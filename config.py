import os
from aiogram.enums import ParseMode

BOT_TOKEN = os.getenv("8440054063:AAFd3bFruBbKoGOb2Hf63uluEnvnI_UZ23o")
MONGO_URI = os.getenv("mongodb+srv://nexacoders2_db_user:dxYh7QOdHvH6OVdd@cluster0.f4qxcbk.mongodb.net/?appName=Cluster0")

ADMINS = [int(x) for x in os.getenv("ADMINS", "8230040205,8580367479").split(",") if x]

BOT_USERNAME = os.getenv("VLRVOTEBOT")  # without @

START_IMAGE = "https://i.ibb.co/Kzqvs15M/477fc36ddaa7.jpg"
PARTICIPANT_IMAGE = "https://files.catbox.moe/xj0ci0.jpg"

PARSE_MODE = ParseMode.HTML
