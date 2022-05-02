import logging
import requests

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update, _):
    keyboard = [
        [
            InlineKeyboardButton("FAQ", callback_data='1'),
            InlineKeyboardButton("Купить билеты", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Что Вам интересно?:', reply_markup=reply_markup)


def button(update, _):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы.
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # редактируем сообщение, тем самым кнопки
    # в чате заменятся на этот ответ.
    if variant == '1':
        query.edit_message_text(text="1. Каков режим работы музея? Музей открыт для посещений: с 8:30 до 16:30, без "
                                     "выходных перерыв с 12:00 до 13:00. Каждый последний понедельник месяца музей "
                                     "закрыт на санитарный день. Предварительную заявку на посещение можно сделать по "
                                     "телефону 8 (863-51) 9-23-37 (экспозиционно-этнографический отдел), 9-27-97 (отдел "
                                     "исследования творческого наследия А.В Калинина, в х. Пухляковский по пер. "
                                     "Городской,14), 9-21-64 (директор музея). 2. Как заказать экскурсию? Экскурсии "
                                     "проводятся постоянно, в рабочее время . Экскурсию можно выбрать и оплатить на "
                                     "официальном сайте музея http://museum-razdory.ru, в разделе «Посетителям». Так же"
                                     " выбрать и оплатить экскурсию можно при личном посещении, в кассе музея. "
                                     "Предварительную заявку на экскурсионное посещение можно сделать по телефону "
                                     "8 (863-51) 9-23-37 (экспозиционно-этнографический отдел), 9-27-97 (отдел "
                                     "исследования творческого наследия А.В Калинина, в х. Пухляковский по "
                                     "пер. Городской,14), 9-21-64 (директор музея). 3. Какова стоимость входного билета?"
                                     " С ценами на посещение музея и другими услугами вы можете ознакомиться на "
                                     "официальном сайте музея, в разделе «Стоимость и льготы». 4. Что включено в "
                                     "стоимость входного билета? С перечнем оказываемых музеем услуг и их описанием, "
                                     "вы можете ознакомиться на официальном сайте музея, в разделе «Стоимость и льготы»."
                                     " 5. Есть ли льготные билеты? С положением о порядке льготного и бесплатного "
                                     "посещения музея, вы можете ознакомиться на официальном сайте музея, в разделе "
                                     "«Стоимость и льготы». 6. Как добраться до музея? В ст. Раздорской Усть-Донецкого"
                                     " района расположено 4 выставочных центра с экспозициями и выставками: - "
                                     "ул. Ленина, 42 – Выставочный центр в здании «Дом торгового казака Устинова» - "
                                     ". Ленина, 42 «а» – Выставочный центр в здании «Жилой дом с торговой лавкой казака "
                                     "Гуськова» - ул. Ленина, 48 – Выставочный центр в здании «Казачий курень» - "
                                     ". Ленина, 50 – КАССА и выставочный центр в здании «Церковно-приходская школа» В "
                                     "х. Пухляковский Усть-Донецкого района расположено 3 выставочных центра с "
                                     "экспозициями и выставками: - пер. Городской, 14, Выставочный центр «История "
                                     "виноделия на Дону» - ул. Центральная 116 – Выставочный центр «А.В. Калинин: "
                                     "человек, писатель, гражданин» - ул. Строителей, 1 – выставка «Пухляковская "
                                     "картинная галерея. Возрождение» 7. Можно ли фотографировать в музее? Да, можно "
                                     "осуществлять любительскую съемку за отдельную плату. С перечнем оказываемых музеем"
                                     " услуг и их описанием, вы можете ознакомиться на официальном сайте музея, в "
                                     "разделе «Стоимость и льготы». 8. Нужна ли сменная обувь на экскурсии? Нет, сменная"
                                     " обувь не является обязательной. При необходимости, на входе выдаются бахилы. 9. "
                                     "Каковы правила посещения музея? С правилами посещения музея вы можете ознакомиться"
                                     " на официальном сайте музея, в разделе «Документы».")
    elif variant == '2':
        query.edit_message_text(text="https://vmuzey.com/museum/razdorskiy-etnograficheskiy-muzey-zapovednik")

    elif variant == '3':
        query.edit_message_text(text="https://vmuzey.com/museum/razdorskiy-etnograficheskiy-muzey-zapovednik")


def help_command(update, _):
    update.message.reply_text("Используйте `/start` для тестирования.")


def print_news(update, context):
    a = int(context.args[0])

    with open('all_news.txt', encoding='utf-8') as f:
        data = list(map(str.strip, f.readlines()))

    if len(data) > a:
        url = f'http://museum-razdory.ru/about/news.php?ELEMENT_ID={data[a]}'
        response = requests.get(url)

        t = response.text
        f_text = '<!-----  ПОЛНЫЙ ТЕКСТ   ----->'
        f = t.find(f_text)
        s_text = "Возврат к списку"
        s = t.find(s_text)
        all_txt = t[f:s]

        not_in_text = ["</div>", "<br>", "<div>", "<!-----  ПОЛНЫЙ ТЕКСТ   ----->", 'a href="/about/news.php">']
        for i in not_in_text:
            all_txt = all_txt.replace(i, "")

        for i in range(len(all_txt)):
            if len(all_txt) > i:
                if all_txt[i] == "<":
                    zak = all_txt.find(">", i)
                    all_txt = all_txt.replace(all_txt[i:zak + 1], "")

        all_txt = all_txt[:-1]
        text = ' '.join(all_txt.split())
        update.message.reply_text(text)
    else:
        update.message.reply_text("ТАКОЙ НОВОСТИ НЕТ. ПОВТОРИТЕ ПОПЫТКУ")


if __name__ == '__main__':
    # Передайте токен вашего бота.
    updater = Updater("5327336439:AAE_OZh-pYtvxDjHXaVayKpLqYVI9LsZOCo")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler("news", print_news, pass_args=True))

    # Запуск бота
    updater.start_polling()
    updater.idle()
