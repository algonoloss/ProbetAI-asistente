import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F
from firebase_admin import credentials, firestore, initialize_app
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

# Firebase setup
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": FIREBASE_PROJECT_ID,
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_CERT_URL")
})
initialize_app(cred)
db = firestore.client()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("¡Hola! Este es tu bot privado ProBetAI Asistente.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
