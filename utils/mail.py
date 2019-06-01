import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import CONFIG
import sentry_sdk

# Replace sender@example.com with your "From" address.
# This address must be verified.
SENDER = CONFIG.get("SMTP_MAIL")
SENDERNAME = 'Log Responses'

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = CONFIG.get("SMTP_RESPONSE")

# Replace smtp_username with your Amazon SES SMTP user name.
USERNAME_SMTP = CONFIG.get("SMTP_USERNAME")

# Replace smtp_password with your Amazon SES SMTP password.
PASSWORD_SMTP = CONFIG.get("SMTP_PASSWORD")

# (Optional) the name of a configuration set to use for this message.
# If you comment out this line, you also need to remove or comment out
# the "X-SES-CONFIGURATION-SET:" header below.
CONFIGURATION_SET = "ConfigSet"

# If you're using Amazon SES in an AWS Region other than US West (Oregon),
# replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP
# endpoint in the appropriate region.
HOST = CONFIG.get("SMTP_SERVER")
PORT = CONFIG.get("SMTP_PORT")


class Mail():
    def __init__(self, url, status):
        # The subject line of the email.
        SUBJECT = "Alerta! {0}".format(url)

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = ("Amazon SES Test\r\n"
                     "This email was sent through the Amazon SES SMTP "
                     "Interface using the Python smtplib package."
                     )

        # The HTML body of the email.
        BODY_HTML = "<html><head></head><body><h1>Sistema Fora do Ar!</h1><p>Informamos que o domínio a baixo econtra-se inacessível.</p><p>URL: {0}<br/>Último Status: {1}</body></html>".format(url, status)

        # Create message container - the correct MIME type is multipart/alternative.
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = SUBJECT
        self.msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
        self.msg['To'] = RECIPIENT
        # Comment or delete the next line if you are not using a configuration set
        # self.msg.add_header('X-SES-CONFIGURATION-SET', CONFIGURATION_SET)

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(BODY_TEXT, 'plain')
        part2 = MIMEText(BODY_HTML, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        self.msg.attach(part1)
        self.msg.attach(part2)

    def send_mail(self):
        # Try to send the message.
        try:
            server = smtplib.SMTP(HOST, PORT)
            server.ehlo()
            server.starttls()
            #stmplib docs recommend calling ehlo() before & after starttls()
            server.ehlo()
            server.login(USERNAME_SMTP, PASSWORD_SMTP)
            server.sendmail(SENDER, RECIPIENT, self.msg.as_string())
            server.close()
        # Display an error message if something goes wrong.
        except Exception as e:
            if CONFIG.get("SENTRY_URL") != "":
                sentry_sdk.init(CONFIG.get("SENTRY_URL"))
                sentry_sdk.capture_exception(e)
        else:
            print("Email sent!")
