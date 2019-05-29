import requests
from urls import sites
from model.log import Log
import datetime
from model.dao import Dao
from utils.mail import Mail
from config import CONFIG
import sentry_sdk


def main():
    #print(CONFIG.get("SMTP_SERVER"))
    #if CONFIG.get("SENDMAIL"):
    #    mail = Mail()
    #    mail.send_mail()
    loop = 10
    seconds = 0.01
    [threading.Thread(target=worker, args=(loop, seconds, s)).start()
     for s in CONFIG.get("SITES_HEALTHCHECK")]


def worker(loop, seconds, url):
    i = 1
    dao = Dao()
    while(i <= loop):
        print('check => ', url, 'i => ', i)
        try:
            start = time.time()
            request = requests.get(url, timeout=CONFIG.get("REQUEST_TIMEOUT"))
            status_code = request.status_code
        except Exception as e:
            if CONFIG.get("SENTRY_URL") != "":
                sentry_sdk.init(CONFIG.get("SENTRY_URL"))
                sentry_sdk.capture_exception(e)
            status_code = CONFIG.get("REQUEST_DEFAULT_ERROR")

        try:
            dao.insert(log_entity(url, status_code, (time.time() - start)))
        except Exception as e:
            if CONFIG.get("SENTRY_URL") != "":
                sentry_sdk.init(CONFIG.get("SENTRY_URL"))
                sentry_sdk.capture_exception(e)
            sentry_sdk.capture_exception(e)

        i += 1
        time.sleep(seconds)


def log_entity(message, status, response_time, date=datetime.datetime.now()):
    return {"date": date, "message": message, "status": status, "response_time": response_time}

#Dao.all()
#Dao.insert({"date": datetime.datetime.now(), "message": "wwww.google.com", "status": "200"})
#Dao.update("5cec675cf259536da8b1df07", { "message": "uol.com.br" })
#Dao.find("5cec84ca4227f4f9876aadd5")
#Dao.delete("5cec84ca4227f4f9876aadd5")
#Dao.deleteAll()


if __name__ == "__main__":
    main()
