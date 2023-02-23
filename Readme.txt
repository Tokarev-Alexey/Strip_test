Инструкция для Linux:

1. Создать папку и открыть в ней терминал
git init                      # создаём репозиторий в этой директории

2. git clone git@github.com:Tokarev-Alexey/Stripe_test.git # слонируем репозиторий GitHub

3. Заходим в папку Stripe_test и открываем в ней терминал
python3 -m venv venv           # создаем виртуальное окружение

4. source venv/bin/activate       # создаем виртуальное окружение

5. pip install -r requirements.txt   # активируем его

6. python3 manage.py runserver   # запускаем проект и переходи по предложенной ссылке для ручного тестирования задания

ИЛИ

Запускаем через Docker:

Проделываем действия 1-2.

В папке проекта открываем терминал:
docker build --tag stripe-test . # создаем образ проекта

docker run -it -p 8000:8000 stripe-test # запускаем в интерактивном режиме и тестим по предложенной ссылке

