from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("mysql+pymysql://student:1q2w#E$R@nadejnei.net:33306/test")

metadata = MetaData()
con = engine.connect()
telsprav = Table('telsprav', metadata,
                  Column('id', Integer, autoincrement=True, primary_key=True),
                  Column('name', String(30), nullable=False, index=True),
                  Column('surname', String(30), nullable=False),
                  Column('sex', String(1), nullable=False),
                  Column('phone', String(20),nullable=False)
                 )


sel1 = telsprav.select()

result = con.execute(sel1)
print(result.fetchone())