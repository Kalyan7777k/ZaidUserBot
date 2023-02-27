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
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAJ5H78ZkPI2dDFrytTzyGzA3st65zNWVwuwlNuP0GpnJp5peI96MrRrUUgJOpoSWoDBJoPpIDo2euS6AUZyVEs4qUbecQa0vr3OIWMLTYsYucolK27B09WIuH3ICTor6hddZhijHh5H3hUAhmpDGHRV8eZToNMYQLpk9w-n3iHVKTDhb8Scld4FISykyEHbsrleOrBlYbOQzUsnLTBS8mOQYJej2edqGNam88afE2tumIPHCnt096mYl-pECt1q-7N0HgCXoYlU7bQbYCAwCUKRK0t8HZ2pFsqm__aXtfdJhYoWksUG3r0vz5s2wonT6-wJ2tdPC4ftTQUTr_ppqVQgAAAAFRFeYgAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
