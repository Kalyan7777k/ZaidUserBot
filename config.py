import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25566413")) #optional
API_HASH = getenv("API_HASH", "5f4dcf21daeac7c01bb229e3e3349f3d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5655356960").split()))
OWNER_ID = int(getenv("OWNER_ID",  "5655356960"))
MONGO_URL = getenv("MONGO_URL",  "mongodb+srv://mongodb+srv://king777:kalyan@cluster0.zco8nze.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6115865751:AAEZ-po4tJi1eWOYbvuIdbe3ZfyIePuwgw8")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/813f420efc5937fcb200d.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT",  "kalyan babu")
PM_LOGGER = getenv("PM_LOGGER" 'https://telegra.ph/file/8d1889f0b73cec790f97a.jpg')
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAfxnJ6qYAnC84VSqvuUSI_Er03iNIp9DiFnZA8mss13pnLfjBL9gJF6aM5XTXDnGeDLQdgxHIn88fQcIM2tcBbi7i71zRyA_3Zo1erUrn0fQkSWmL1rc_9BLrazdtD1V2xyoqkdo6HBPcDFT2Mdvfu4RJA7dx1F3c61MYaeOVziI7UfXEm9j5KHJ-MW7oH11qnKxQjrrQnJktZdXXKcGTVKmxlVwGHmRhwZJ8qSt6u-DxrFwBHgcYF0fhUL9ZDBzIwQf0ZBuehHUeMKofeZPx17v_2ewZOijcw9yWUDIw31rdXnonsV1SrBQgrYuJDTj9cPrYYy96Lxl2jmP78SV2rgAAAAFRFeYgAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
