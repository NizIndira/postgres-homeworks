"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import pandas

connection = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="1501"
)

cursor = connection.cursor()

data = pandas.read_csv(r'north_data/employees_data.csv')
df = pandas.DataFrame(data)

for row in df.itertuples():
    cursor.execute(
        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)"
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (row[1], row[2], row[3], row[4], row[5], row[6])
        )

data = pandas.read_csv(r'north_data/customers_data.csv')
df = pandas.DataFrame(data)

for row in df.itertuples():
    cursor.execute(
        "INSERT INTO customers (customer_id, company_name, contact_name)"
        "VALUES (%s, %s, %s)",
        (row[1], row[2], row[3])
        )

data = pandas.read_csv(r'north_data/orders_data.csv')
df = pandas.DataFrame(data)

for row in df.itertuples():
    cursor.execute(
        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)"
        "VALUES (%s, %s, %s, %s, %s)",
        (row[1], row[2], row[3], row[4], row[5])
        )

connection.commit()