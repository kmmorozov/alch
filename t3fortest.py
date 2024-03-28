from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, Column, DateTime, ForeignKey, Numeric,
                        CheckConstraint, Insert)

engine = create_engine("mysql+pymysql://student:1q2w#E$R@nadejnei.net:33306/test2")

metadata = MetaData()
con = engine.connect()

users = Table('users', metadata,
              Column('id', Integer, autoincrement=True, primary_key=True),
              Column('username', String(20), nullable=False),
              Column('first_name', String(20), nullable=False),
              Column('last_name', String(30), nullable=False)
              )
user_contacts = Table('usercontacts', metadata,
                      Column('id', Integer, autoincrement=True, primary_key=True),
                      Column('user_id', Integer, ForeignKey('users.id')),
                      Column('email', String(50), nullable=True),
                      Column('phone', String(20), nullable=True)
                      )

right_list = Table('rightlist', metadata,
                   Column('id', Integer, autoincrement=True, primary_key=True),
                   Column('right', String(10), nullable=False)
                   )

user_rights = Table('userrighst', metadata,
                    Column('id', Integer, autoincrement=True, primary_key=True),
                    Column('user_id', Integer, ForeignKey('users.id')),
                    Column('rights', Integer, ForeignKey('rightlist.id'))
                    )

ins2 = Insert(users).values(
    username = 'morozovk',
    first_name ='Kirill',
    last_name ='Morozov'
)

metadata.create_all(engine)
con.commit()
con.execute(ins2)
con.commit()
