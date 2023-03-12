from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


"""Callback buttons"""
reserve_btn = InlineKeyboardButton('Записаться', callback_data='Записаться')
cancel_btn = InlineKeyboardButton('Отмена', callback_data='cancel_btn')
contact_btn = InlineKeyboardButton('Контакты', callback_data='contact_btn')
price_btn = InlineKeyboardButton('Прайс', callback_data='price_btn')
schedule_btn = InlineKeyboardButton('Расписание', callback_data='schedule_btn')
menu_markup = InlineKeyboardMarkup(row_width=2)
menu_markup.add(reserve_btn, cancel_btn, contact_btn, price_btn, schedule_btn)

"""URL buttons"""
url_btn_order = InlineKeyboardButton(text='Записаться', url='https://n827632.yclients.com/')
url_btn_inst = InlineKeyboardButton(
    text='Наш инстаграм',
    url='https://instagram.com/akinfeeva_nails?igshid=YmMyMTA2M2Y='
    )
url_btn_location = InlineKeyboardButton(text='Где мы находимся', url='https://go.2gis.com/sj3uo')
url_buttons = InlineKeyboardMarkup(row_width=2)
url_buttons.add(url_btn_order, url_btn_inst, url_btn_location)

"""Messages"""
start_message = 'Привет! Я бот салона Akinfeeva Nails!\n' \
                'Знаем всё про крепкие и красивые ногти!\n' \
                'ИДЕАЛЬНЫЙ МАНИКЮР ЗА 1.5 часа 🚀\n' \
                'ПЕРВЫЙ РАЗ? Скидка 200р. на первое посещение\n' \
                'Запись в один клик❤️\n' \
                'Выбери, что ты хочешь сделать 💅🏼'
welcome_message = 'Привет, если вам нужен качественный маникюр или педикюр, то вы пришли по адресу!\n'
date_message = 'Когда Вы хотите записаться на прием? (в формате ДД.ММ.ГГГГ)'
wrong_date_message = 'Неверный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ'
need_correct_date_message = 'Введите предстоящую дату, записаться в прошлое, увы невозможно)'
time_message = 'На какое время вы хотели бы записаться? Напишите в формате ЧЧ:ММ'
uncorrect_time_message = 'Неверный формат времени. Пожалуйста, введите время в формате ЧЧ:ММ'
phone_message = 'Напишите свой номер телефона для связи'

