import pymysql.constants.FLAG
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, CheckConstraint, insert
from datetime import datetime

metadata = MetaData()
engine = create_engine("mysql+pymysql://student:1q2w#E$R@nadejnei.net:33306/test")
#engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")

customers = Table('customers', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('username', String(50), nullable=False),
    Column('email', String(200), nullable=False),
    Column('address', String(200), nullable=False),
    Column('town', String(50), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


items = Table('items', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
    Column('cost_price', Numeric(10, 2), nullable=False),
    Column('selling_price', Numeric(10, 2),  nullable=False),
    Column('quantity', Integer(), nullable=False),
    CheckConstraint('quantity > 0', name='quantity_check')
)


orders = Table('orders', metadata,
    Column('id', Integer(), primary_key=True),
    Column('customer_id', ForeignKey('customers.id')),
    Column('date_placed', DateTime(), default=datetime.now),
    Column('date_shipped', DateTime())
)


order_lines = Table('order_lines', metadata,
    Column('id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.id')),
    Column('item_id', ForeignKey('items.id')),
    Column('quantity', Integer())
)


metadata.create_all(engine)

ins = customers.insert().values(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko',
    username = 'Moseend',
    email = 'moseend@mail.com',
    address = 'Shemilovskiy 2-Y Per., bld. 8/10, appt. 23',
    town = ' Vladivostok'
)

print(ins) # Показать шаблон запроса
print(ins.compile().params) # показать релаьный инсерт с данными
connection = engine.connect()
execute_result = connection.execute(ins) # выполнить запрос
print(execute_result.inserted_primary_key) # result имеет ряд атрибутов
connection.commit() # Выполнить commit
# второй способ insert  требует импорта insert

ins2 = insert(customers).values(
    first_name = 'Valeriy',
    last_name = 'Golyshkin',
    username = 'Fortioneaks',
    email = 'fortioneaks@gmail.com',
    address = 'Narovchatova, bld. 8, appt. 37',
    town = 'Magadan'
)
r = connection.execute(ins2)
print(r.inserted_primary_key)

ins3 = insert(customers)

#  передавать данные можно списком
r = connection.execute(ins3, [
        {
            "first_name": "Vladimir",
            "last_name": "Belousov",
            "username": "Andescols",
            "email":"andescols@mail.com",
            "address": "Ul. Usmanova, bld. 70, appt. 223",
            "town": " Naberezhnye Chelny"
        },
        {
            "first_name": "Tatyana",
            "last_name": "Khakimova",
            "username": "Caltin1962",
            "email":"caltin1962@mail.com",
            "address": "Rossiyskaya, bld. 153, appt. 509",
            "town": "Ufa"
        },
        {
            "first_name": "Pavel",
            "last_name": "Arnautov",
            "username": "Lablen",
            "email":"lablen@mail.com",
            "address": "Krasnoyarskaya Ul., bld. 35, appt. 57",
            "town": "Irkutsk"
        },
    ])
connection.commit()

# можно предварительно создать список, потом скормить его connection.execute(insert(customers),customers_list)
customers_list = [
    {
        "first_name": "Kirill",
        "last_name": "Morozov",
        "username": "morozovk",
        "email": "kmmorozov@mail.com",
        "address": "Sovetskiy prospekt 41 kv 450",
        "town": "SPB"
    }
]

connection.execute(insert(customers),customers_list)
connection.commit()

####################
# Заполнение таблиц

# items_list = [
#     {
#         "name":"Chair",
#         "cost_price": 9.21,
#         "selling_price": 10.81,
#         "quantity": 6
#     },
#     {
#         "name":"Pen",
#         "cost_price": 3.45,
#         "selling_price": 4.51,
#         "quantity": 3
#     },
#     {
#         "name":"Headphone",
#         "cost_price": 15.52,
#         "selling_price": 16.81,
#         "quantity": 50
#     },
#     {
#         "name":"Travel Bag",
#         "cost_price": 20.1,
#         "selling_price": 24.21,
#         "quantity": 50
#     },
#     {
#         "name":"Keyboard",
#         "cost_price": 20.12,
#         "selling_price": 22.11,
#         "quantity": 50
#     },
#     {
#         "name":"Monitor",
#         "cost_price": 200.14,
#         "selling_price": 212.89,
#         "quantity": 50
#     },
#     {
#         "name":"Watch",
#         "cost_price": 100.58,
#         "selling_price": 104.41,
#         "quantity": 50
#     },
#     {
#         "name":"Water Bottle",
#         "cost_price": 20.89,
#         "selling_price": 25.00,
#         "quantity": 50
#     },
# ]
#
# order_list = [
#     {
#         "customer_id": 1
#     },
#     {
#         "customer_id": 1
#     }
# ]
#
# order_line_list = [
#     {
#         "order_id": 1,
#         "item_id": 1,
#         "quantity": 5
#     },
#     {
#         "order_id": 1,
#         "item_id": 2,
#         "quantity": 2
#     },
#     {
#         "order_id": 1,
#         "item_id": 3,
#         "quantity": 1
#     },
#     {
#         "order_id": 2,
#         "item_id": 1,
#         "quantity": 5
#     },
#     {
#         "order_id": 2,
#         "item_id": 2,
#         "quantity": 5
#     },
# ]
#
# r = connection.execute(insert(items), items_list)
# print(r.rowcount)
# r = connection.execute(insert(orders), order_list)
# print(r.rowcount)
# r = connection.execute(insert(order_lines), order_line_list)
# print(r.rowcount)





