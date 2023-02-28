import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25566413")) #optional
API_HASH = getenv("API_HASH", "5f4dcf21daeac7c01bb229e3e3349f3d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5655356960").split()))
OWNER_ID = int(getenv("OWNER_ID",  "5655356960"))
MONGO_URL = getenv("MONGO_URL",  "mongodb+srv://babukalyan977:babukalyan977@cluster0.fvkyo4r.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6266931054:AAEkvXmVTL7wMLlgjwBCq1_aXgpG0kg6Q3g")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT",  "kalyan babu")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAAtbZW40936n6Eb93nFHuu0Pt-NKrxnFDrHk98M5hnkEGa3onOkpmtAqCEkEbxtPZnCroW_SpRDjRpT42jSKSFm5rpvs6E-AitjbAlKu2X_6aebjoj60iSc9taCVPCbw-9NV6_4Xb-DQxWJblY9JthmWQkI2mIgGxpNxhtmZED0Ps3bVLLmGBcDLsiQtYIX8S2Slap453vM23jP1nXyfNelF6xVdAHmFRVN7mT1MNCoh_aEE8ANgbLpGzqvFKbf6U0_diMtbRrDGoMOFu7luq--WDIONWmWpAbQnaZSD4_TJR332gp2zkBaDodbFtHM7hw3tGKOICdYtX0VOdnD-LiQAAAAFRFeYgAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
