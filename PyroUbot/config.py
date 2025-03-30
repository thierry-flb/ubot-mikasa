import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("ZEX", "6530352261").split()))

API_ID = int(os.getenv("API_ID", ""))

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("7835831296:AAG-kePOd3oDhwPTk_6H7n3WZ6u7sw5cSs0", "")

OWNER_ID = int(os.getenv("6530352261", ""))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002341528178").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))
