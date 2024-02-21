#Github.com/mrinvisible7

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "24192661"
API_HASH = "810a6dc0b2c2bf4db55db3a9ad999b56"
BOT_TOKEN = "6259718751:AAEjFAu83hn_tDDZS8-8kG5nMgDzR1vhviA"
SESSION = "BQFxJpUAkficUxLy-GcvkHAteqCiJryHJJuST7y1T2jGLAWfDQ91SVRv6Ri7Hunzevfa5SS4GZu787HPtyad4ElDb82gdbveRovUk85mmOM1w0JmaYTsaWmPosXzuQDCsUohMrsZ27V_JJ3keidVaZEAd76SHYUgNEPobN2_amGo9unFyNO7y_YvFOpYE63m5WKNM_ALs_sviFxSlMWh2iuHb4EWdVcZNI_rBkuOXyU6yKYJRXIiAinrB1kwbALi2_otDe2NwRx2z3XHizlIQ9qYMD47LS9VD4N8kn-EMQmxW_URyYa3XNISDKGYJu-YKO6bwAMDp5K3mqcjbPUQL4yjx0xMWQAAAAFDgwaAAA"
FORCESUB = "raoji47"
AUTH = "5427627648"
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
