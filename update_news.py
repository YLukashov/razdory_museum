import requests
from bs4 import BeautifulSoup
import re

url = f'http://museum-razdory.ru/about/news.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

t = response.text
begin_of_array = t.find("[ELEMENTS] => Array")
end_of_array = t.find("[NAV_STRING] => ")
all_str = t[begin_of_array:end_of_array]

num = re.findall(r'\d+', all_str)

all_news = list(filter(lambda x: len(x) > 3, num))

with open('all_news.txt', 'w', encoding='utf-8') as d:
    for i in all_news:
        d.write(i)
        d.write('\n')

print(all_news)