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
