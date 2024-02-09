from fastapi import FastAPI
import pymysql
import datetime
import time
import redis
app = FastAPI()


def connect_to_db(host, port, user, password, db):
    connection = pymysql.connect(host='172.20.10.13', port=306, user='obmen', password='123456', db='bank')
    cursor = connection.cursor()
    return connection, cursor


def get_valute_rate_from_db(connection, cursor, valute):
    today = datetime.datetime.now().strftime('%Y%m%d')
    select_str = f'SELECT rate  from valute_rate  WHERE valute = "{valute}" AND  date  = "{today}";'
    cursor.execute(select_str)
    rate = float(cursor.fetchall()[0][0])
    return rate

@app.get("/users")
def root():
    return 'sasha, dasha'

@app.get("/valutes{valute_name}")
def get_valute_rate(valute_name):
    connection, cursor = connect_to_db()
    rate = get_valute_rate_from_db(connection, cursor, valute_name)
    return {valute_name:rate}


@app.get("/convert")
def convert_valute(fv, sv, count):
    st = int(count)
    time.sleep(st)
    return fv, sv, count

#сдеелать чтобы конверт возвращал сколько нужно возвращать валюты
#
