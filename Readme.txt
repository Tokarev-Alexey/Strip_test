Инструкция для Linux:

Создать папку и открыть в ней терминал

git init                      # создаём репозиторий в этой директории

git clone git@github.com:Tokarev-Alexey/Stripe_test.git # слонируем репозиторий GitHub

Заходим в папку Stripe_test и открываем в ней терминал

python3 -m venv venv           # создаем виртуальное окружение

source venv/bin/activate       # создаем виртуальное окружение

pip install -r requirements.txt   # активируем его

python3 manage.py runserver   # запускаем проект и переходи по предложенной ссылке для ручного тестирования задания

ИЛИ


