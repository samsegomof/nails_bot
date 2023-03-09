import logging

from aiogram import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import BOT_TOKEN

"""Файл инициализации и запуска бота"""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class StateMachine(StatesGroup):
    name_waiting = State()
    date_waiting = State()
    time_waiting = State()
    phone_waiting = State()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
