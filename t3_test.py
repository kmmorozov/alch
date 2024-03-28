from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, CheckConstraint
from datetime import datetime

metadata = MetaData()
engine = create_engine("mysql+pymysql://student:1q2w#E$R@nadejnei.net:33306/test")

telsprav = Table('telsprav', metadata,
                 Column('id', Integer, autoincrement=True, primary_key=True),
                 Column('name', String(30), nullable=False, index=True),
                 Column('surname', String(30), nullable=False),
                 Column('sex', String(1), nullable=False),
                 Column('phone', String(20),nullable=False)
                 )

metadata.create_all(engine)

ins = telsprav.insert().values(
    name = 'Kirill',
    surname = 'Morozov',
    sex = 'm',
    phone = '89110281345'
)

print(ins)
conn = engine.connect()
result = conn.execute(ins)
conn.commit()
print(result)