## Телеграм Бот для записи клиентов к мастеру ногтевого сервиса
### Описание:
Данный проект представляет собой телеграм-бота для записи на прием к мастеру. Пользователь может отправить свое имя, дату и время приема, а также номер телефона. Данные записываются в базу данных SQLite, после чего мастеру отправляется уведомление о новой записи. Код написан на языке Python с использованием библиотеки aiogram для создания телеграм-бота и sqlite3 для работы с базой данных.

Класс Database содержит методы для создания таблицы в базе данных и добавления новых записей в эту таблицу. В файле actions.py определены обработчики сообщений, которые получает бот. Обработчик для команды /start начинает процесс записи, переводя пользователя в состояние name_waiting, где он должен отправить свое имя. Затем следует последовательность состояний date_waiting, time_waiting и phone_waiting, где пользователь отправляет дату, время и номер телефона соответственно. После получения номера телефона происходит запись данных в базу данных и отправка уведомления мастеру о новой записи.

Файл запуска бота bot.py содержит функции для создания объектов Bot и Dispatcher, а также запуска бота с использованием метода executor.start_polling.

Код написан в стиле объектно-ориентированного программирования и с использованием концепции состояний (FSM).