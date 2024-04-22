# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


    API_ID = int(os.environ.get("API_ID", "20919286"))
    API_HASH = os.environ.get("API_HASH", "57b85f72104db3f08f9795b0410eb556")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7101381082:AAGQQrFIDpGgSyi_voDJ-JoTv4hRIPmwRo0")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 6976445947))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "6976445947").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://sasikumaris010:sasikumaris010@cluster0.tiplcqn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002124243193"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
