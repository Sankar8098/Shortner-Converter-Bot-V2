# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23990433"))
API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6181493706:AAE4GDBtYO9To_LOO-qSZU79_ABxtE-_M3A")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "nakflixbot")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://sankar:sankar@sankar.lldcdsx.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5821871362")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1255023013)

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001870015374")) 

# For Force Subscription
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "SK_MoviesOffl")

# true if forward should be avoided
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True")

# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = "False"
