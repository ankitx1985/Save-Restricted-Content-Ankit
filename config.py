# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "26994377")
API_HASH = os.getenv("API_HASH", "9c9eb74a4a0a1ecd4c96abebf3c637ee")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8287122600:AAEYa9CSs1MF4Rsi48CsfDdXJEhs64P2YX0")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://fixmayart834:FMWwXBd4JJYMs2Iv@cluster0.ltpube9.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "8184789731").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegramkibot")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002936339662")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1003024428633")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "0758b508da4624ad14ce7f4cc21b3c1d") # for session encryption
IV_KEY = os.getenv("IV_KEY", "36511fdfe71c") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "50"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "10000"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/Heisenberg_Universe") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/Heisenbergsells")

