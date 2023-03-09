import os

from dotenv import load_dotenv

load_dotenv()   # Функция для загрузки переменных из .env

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
MASTER_CHAT_ID = os.getenv('MASTER_CHAT_ID')  # chat_id мастера
