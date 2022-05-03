import requests


def print_exhibit(update, context):
    a = int(context.args[0])

    with open('all_exhibitions.txt', encoding='utf-8') as f:
        data = list(map(str.strip, f.readlines()))

    if len(data) > a:

        url = f'http://museum-razdory.ru/exhibitions/?ELEMENT_ID={data[a]}'
        response = requests.get(url)
        t = response.text
        f_text = '<!-----  ПОЛНЫЙ ТЕКСТ   ----->'
        f = t.find(f_text)
        s_text = "Время работы: ежедневно, с 8.30 до 16.30 часов."
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
        if text[0] == "<":
            zak = text.find(">")
            text = text.replace(text[0:zak + 1], "")
        print(text)
    else:
        update.message.reply_text("НОМЕРА С ТАКОЙ ВЫСТАВКОЙ НЕТ. ПОВТОРИТЕ ПОПЫТКУ")
