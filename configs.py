# (c) @TumaraBaap • @RymOfficial

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "24300561"))
    API_HASH = os.environ.get("API_HASH", "c6c32708e5cc87f09110cb1e1121ff1a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5757456336:AAFa-VXqoxBuQwMBjsajAsoewEJQb3_306w")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "1637312289"))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://ETYrequest3:ETYrequest3@cluster0.8ur6aqw.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001637312289"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
