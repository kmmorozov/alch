
from sqlalchemy import create_engine, MetaData, Table, Integer, String, asc, desc, Column, DateTime, ForeignKey, Numeric, CheckConstraint, insert, select, not_ , func
from datetime import datetime

# https://pythonru.com/biblioteki/crud-sqlalchemy-core
metadata = MetaData()
engine = create_engine("mysql+pymysql://student:1q2w#E$R@nadejnei.net:33306/test")
# engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")

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
              Column('selling_price', Numeric(10, 2), nullable=False),
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

# Условия при выборках
# 1 Вариант
s = select(customers).where(customers.c.id < 10).where(customers.c.first_name == 'Dmitriy')

connection = engine.connect()

result = connection.execute(s)

# print(result.fetchall())

# Второй вариант
# s = select(customers).where((customers.c.id > 10) & ((customers.c.first_name == 'Kirill') | (customers.c.last_name == 'Morozov'))  )
# s = select(customers).where((customers.c.id > 10) & ((customers.c.first_name == 'Kirill') or (customers.c.last_name == 'Morozov'))  )
# s = select(customers).where((customers.c.id > 10) & ((customers.c.first_name == 'Kirill') or (customers.c.last_name.like('moro%'))) )
# s = select(customers).where((customers.c.id.between(10,16)))
# пример с сортировками
#s = select(customers).where(not_(customers.c.last_name.like("moro%"))).order_by(asc(customers.c.id))
#пример с ограничением колонок
#s = select(customers.c.id, customers.c.first_name).where(not_(customers.c.last_name.like("moro%"))).order_by(desc(customers.c.id))
#s = select([customers]).where(customers.c.first_name.in_(["Valeriy", "Vadim"])) не работает in_ и notin_


# Сортировка
#s = select(customers).order_by(asc(customers.c.id)) # по возрастанию
#s = select(customers).order_by(desc(customers.c.id)) # по убыванию
# Лимит выборки
#s = select(customers).limit(2) #  Выбрать 2 записи
#s = select(customers).limit(2).offset(3) #  Выбрать 2 записи начиная с 3
#Группировка
print('------------------------------------------------------------------------------')
sm = select(func.count(customers.c.id)).group_by(customers.c.first_name).where(customers.c.first_name.like('%'))
# Функции на примере PGSQL
# c = [
#
#     ##  функции даты/времени  ##
#
#     func.timeofday(),
#     func.localtime(),
#     func.current_timestamp(),
#     func.date_part("month", func.now()),
#     func.now(),
#
#     ##  математические функции  ##
#
#     func.pow(4, 2),
#     func.sqrt(441),
#     func.pi(),
#     func.floor(func.pi()),
#     func.ceil(func.pi()),
#
#     ##  строковые функции  ##
#
#     func.lower("ABC"),
#     func.upper("abc"),
#     func.length("abc"),
#     func.trim("  ab c  "),
#     func.chr(65),
# ]
#
# Аргегирующие функции
c = [
    func.sum(customers.c.id),
    func.avg(items.c.quantity),
    func.max(items.c.quantity),
    func.min(items.c.quantity),
    func.count(customers.c.id),
]



# s = select(c)

result2 = connection.execute(sm)






# получение данных из курсора

#print(result2.fetchone()) # выбрать один
print(result2.fetchall()) #  выбрать все
#print(result2.fetchmany(size=2)) # выбрать несколько
#print(result2.first()) # выбрать первую и отключиться, следующие не получить
#print(result2.rowcount)
