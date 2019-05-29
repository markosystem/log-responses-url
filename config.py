import os
from dotenv import load_dotenv
import json

load_dotenv()

CONFIG = {}

CONFIG["MONGO_HOST"] = os.getenv("MONGO_HOST")
CONFIG["MONGO_DB"] = os.getenv("MONGO_DB")
CONFIG["REQUEST_TIMEOUT"] = float(os.getenv("REQUEST_TIMEOUT"))
CONFIG["REQUEST_DEFAULT_ERROR"] = int(os.getenv("REQUEST_DEFAULT_ERROR"))
CONFIG["SITES_HEALTHCHECK"] = json.loads(os.getenv("SITES_HEALTHCHECK"))
CONFIG["SENTRY_URL"] = os.getenv("SENTRY_URL")
CONFIG["SMTP_MAIL"] = os.getenv("SMTP_MAIL")
CONFIG["SMTP_SERVER"] = os.getenv("SMTP_SERVER")
CONFIG["SMTP_RESPONSE"] = os.getenv("SMTP_RESPONSE")
CONFIG["SMTP_PORT"] = os.getenv("SMTP_PORT")
CONFIG["SMTP_USERNAME"] = os.getenv("SMTP_USERNAME")
CONFIG["SMTP_PASSWORD"] = os.getenv("SMTP_PASSWORD")
CONFIG["SENDMAIL"] = bool(os.getenv("SENDMAIL")) or False
