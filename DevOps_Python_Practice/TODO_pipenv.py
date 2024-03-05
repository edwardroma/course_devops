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