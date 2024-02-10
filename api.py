import time

from  fastapi import FastAPI
app = FastAPI()
import pymysql
import logging
import datetime



def get_valute_rate_from_db(connection, cursor, valute):
    logging.debug('Пытаюсь получить сегодняшнюю дату')
    today = datetime.datetime.now().strftime('%Y%m%d')
    logging.debug('Получил сегодняшнюю дату')
    logging.debug('Пытаюсь получить последнюю дату в БД')
    seelect_date_str = 'SELECT date FROM valute_rate ORDER BY date DESC LIMIT 1;'
    cursor.execute(seelect_date_str)
    last_date_in_base = cursor.fetchall()[0][0]
    logging.debug('Получил последнюю дату в БД')
    print('last_date_in_base ', last_date_in_base)
    today = today if today == last_date_in_base else last_date_in_base
    logging.debug('Скорректировал дату для запроса')
    logging.debug('Пытаюсь создать запрос к БД на получение курса валюты')
    select_str = f'SELECT rate  from valute_rate  WHERE valute = "{valute}" AND  date  = "{today}";'
    cursor.execute(select_str)
    logging.debug('Создал запрос к БД на получение курса валюты')
    logging.debug('Пытаюсь получить курс валюты из результатов запроса')
    rate = float(cursor.fetchall()[0][0])
    logging.debug('Получил курс валюты из результатов запроса')
    print('rate ', rate)
    return rate


# def connect_to_db(host, port, user, password, db):
def connect_to_db():
    logging.debug('Пытаюсь создать подключение к БД')
    connection = pymysql.connect(host='192.168.1.46', port=3306, user='obmen', password='123456', db='bank')
    logging.debug('Создал подключение к БД')
    cursor = connection.cursor()
    return connection, cursor


@app.get("/")
def root():
    return 'Привет'

@app.get("/users")
def users():
    return ('раз', 'два', 'три')

@app.get("/valutes/{valute_name}")
def get_valute_rate(valute_name):
    connection, cursor = connect_to_db()
    rate = get_valute_rate_from_db(connection, cursor, valute_name)
    return {valute_name:rate}

@app.get("/convert")
def convert_valute(fv, sv, count):
    st = int(count)
    time.sleep(st)
    return fv, sv , count

# http://127.0.0.1:8000/convert/?fv=USD&sv=EUR&count=1000
# uvicorn api:app --reload
# uvicorn api:app --reload --host 0.0.0.0