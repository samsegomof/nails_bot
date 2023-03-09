import logging
from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram import types

from aiogram import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import BOT_TOKEN, MASTER_CHAT_ID
from accessors.db_accessor import Database
from markups import start_message, date_message, wrong_date_message, \
    need_correct_date_message, time_message, uncorrect_time_message, phone_message

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


async def send_notification_to_master(name: str, date: datetime, time: datetime, phone: str):
    """Функция отправки уведомления мастеру о новой записи"""
    message = (
        f'Новая запись!\n'
        f'Имя: {name}\n'
        f'Дата: {date.strftime("%d.%m.%Y")}\n'
        f'Время: {time.strftime("%H:%M")}\n'
        f'Телефон: {phone}'
    )
    await bot.send_message(chat_id=MASTER_CHAT_ID, text=message)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """Обработчик команды старт"""
    await message.answer(start_message)
    await StateMachine.name_waiting.set()


@dp.message_handler(state=StateMachine.name_waiting)
async def get_name(message: types.Message, state: FSMContext):
    """Обработчик отправки имени"""
    name = message.text
    await state.update_data(name=name)

    await message.answer(date_message)
    await StateMachine.date_waiting.set()


@dp.message_handler(state=StateMachine.date_waiting)
async def get_date(message: types.Message, state: FSMContext):
    """
    Получение даты от пользователя, если формат неверный -
    шлет исключение и просит ввести корректный формат
    """
    try:
        date = datetime.strptime(message.text, '%d.%m.%Y')
    except ValueError:
        await message.answer(wrong_date_message)
    else:
        now = datetime.now()
        if date < now:
            await message.answer(need_correct_date_message)
            return

    await state.update_data(date=date)
    await message.answer(time_message)
    await StateMachine.time_waiting.set()


@dp.message_handler(state=StateMachine.time_waiting)
async def get_time(message: types.Message, state: FSMContext):
    """
    Получение времени от пользователя, если формат неверный -
    шлет исключение и просит ввести верный формат
    """
    try:
        time = datetime.strptime(message.text, '%H:%M').time()
    except ValueError:
        await message.answer(uncorrect_time_message)

    await state.update_data(time=time)
    await message.answer(phone_message)
    await StateMachine.phone_waiting.set()
    return


@dp.message_handler(state=StateMachine.phone_waiting)
async def get_phone(message: types.Message, state: FSMContext):
    """
    Получение номера телефона, запись данных в бд и отправка уведомления мастеру о новой записи
    """
    phone = message.text
    await state.update_data(phone=phone)

    data = await state.get_data()
    name = data.get('name')
    date = data.get('date')
    time = data.get('time')

    await message.answer(
        f'Вы записались на '
        f'{date.strftime("%d.%m.%Y")}\n'
        f'в {time.strftime("%H:%M")}.\n'
        f'Ваше имя: {name}\n'
        f'Ваш номер телефона: {phone}\n'
        f'Я с вами свяжусь по указанному номеру телефона для подтверждения записи!\n'
        f'Если у вам нужно отменить посещение, пожалуйста позвоните по номеру +79875960877'
    )
    with Database('appointments.db') as db:
        db.add_reservation(name, date.strftime('%Y-%m-%d'), time.strftime('%H:%M'), phone)
    await send_notification_to_master(name, date, time, phone)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
