import telebot

TOKEN = '7705375375:AAH_BNOUVpKQzotJDB_5bfhkLPGBtHwQ-Oc'  # Замените на свой токен
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "📌 О компании", "🔗 Все ссылки", 
        "💬 Отзывы", "💼 Партнёрка"
    ]
    for btn in buttons:
        keyboard.add(btn)

    welcome_text = (
        "👋 Приветствуем вас в юридической компании «ЮНОВА»!\n\n"
        "Мы помогаем людям в трудных финансовых ситуациях защищать свои права, "
        "оформлять банкротство и получать качественную юридическую помощь по всей России.\n\n"
        "Выберите интересующий раздел ниже:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    if message.text == "📌 О компании":
        bot.send_message(message.chat.id,
            "📌 *О компании ЮНОВА*\n\n"
            "✅ 3 млрд рублей списанного долга\n"
            "✅ 4700 успешно завершенных дел\n"
            "✅ 10 лет на защите ваших прав\n"
            "✅ Основана в 2014 году\n\n"
            "*Миссия:* защищать законные права граждан по всей РФ, с выдающимся качеством сервиса и настоящей человеческой добротой.",
            parse_mode="Markdown"
        )
    elif message.text == "🔗 Все ссылки":
        bot.send_message(message.chat.id,
            "🔗 *Полезные ссылки:*\n"
            "🌐 Сайт: https://yunova.ru/\n"
            "📘 ВКонтакте: https://vk.com/yunova_samara\n"
            "📢 Телеграм о банкротстве: https://t.me/Levinson_pro_bankrotstvo\n"
            "🎥 Отзывы: https://vkvideo.ru/playlist/-165712534_1",
            parse_mode="Markdown"
        )
    elif message.text == "💬 Отзывы":
        bot.send_message(message.chat.id,
            "📽 *Отзывы наших клиентов:*\n"
            "🎥 https://vkvideo.ru/playlist/-165712534_1\n\n"
            "Убедитесь в качестве нашей работы!"
        )
    elif message.text == "💼 Партнёрка":
        bot.send_message(message.chat.id,
            "💼 *Партнёрская программа ЮНОВА*\n\n"
            "🔹 700 активных партнёров\n"
            "🔹 Выплачено: 17.000.000 ₽\n"
            "🔹 Индивидуальные условия\n"
            "🔹 Высокий процент комиссии\n\n"
            "Хотите зарабатывать с нами? Напишите менеджеру или узнайте подробности на сайте: https://yunova.ru/"
        )
    else:
        bot.send_message(message.chat.id, "❓ Неизвестная команда. Пожалуйста, используйте кнопки ниже.")

bot.polling()
