import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "6000"))

DEVS = list(map(int, os.getenv("ZEX", "6498128655").split()))

API_ID = int(os.getenv("API_ID", ""))

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("7257811101:AAH6GBqDMa1eX3C6mAR_iIbjscsoe1qRJQU", "")

OWNER_ID = int(os.getenv("6498128655", ""))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002341528178").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))
