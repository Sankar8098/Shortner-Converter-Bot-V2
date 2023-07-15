# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23990433"))
API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6390467508:AAEPjEY6IZbkAHx6LtGx3PYiX8J_A-EtNPY")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5821871362")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "nakflixbot")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://nakflixbot:alpha3720@cluster0.qgybxbu.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5821871362")) 
ADMINS.append(5821871362) if OWNER_ID not in ADMINS else []
ADMINS.append(5821871362)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001870015374")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "SK_MoviesOffl") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
