"""Exercise 17 (and Solution) Decode A Web Page"""
import requests
from bs4 import BeautifulSoup
import lxml
from typing import reveal_type

# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.json())

url = "https://google.com"
name = "rocket"
link = requests.get(url)
print(__annotations__)


# def extract_articles(url) -> str:
#     link: requests.get.Response = requests.get(url)
#     soup = BeautifulSoup(link, lxml)
#     link = soup.prettify()
#     return link
#
# print(extract_articles("https://www.nytimes.com/"))

# Use the BeautifulSoup and requests Python packages to print out a list of
#  all the article titles on the New York Times homepage.



###################################

# 2) get_psw_type would better return enum
# (https://docs.python.org/3/library/enum.html).


# 6) Я так понял, у тебя еще где-то рядом с файлом, что ты мне скинул,
# лежат requirements.txt. Для "менеджмента зависимостей" лучше использовать
# Pipenv (https://pipenv.pypa.io/en/latest/). Тут надо прокачаться чуток и
# научиться им пользоваться, но это совсем не сложно, грубо говоря, все сведется
# к следующим командам:
# - pipenv --python 3
# - pipenv install PACKAGE_NAME
# - pipenv uninstall PACKAGE_NAME
# - pipenv run python YOUR_FILE.py
# - pipenv requirements > requirements.txt

# https://ru.wikipedia.org/wiki/Python#%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5

# 9) Можно разбить на "подмодули". Например, WordFinder
# Вместо этого: Сделать класс (и юзать соответственно):
# Это просто логически код разделить Чтобы меньше было похоже на спагетти
# Ну и да, можно вот это преобразование
# ("if less than 3 - should be 2" "if greater than 14 - should be 15")
# в конструкторе выполнить один раз Ну это не обязательно
# Можно password_length передавать в generate_word_list и generate_word_link каждый раз. Это не важно.
# Главный point что я имею в виду - разделение на "логически связанные подмодули"
