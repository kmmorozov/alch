from sqlalchemy import MetaData, ARRAY,  create_engine, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, CheckConstraint
from datetime import datetime
##https://pythonru.com/biblioteki/shemy-sqlalchemy-core
engine = create_engine("mysql+pymysql://student:1q2w#E$R@nadejnei.net:33306/test")
engine.connect()

metadata = MetaData()

blog = Table('blog', metadata,
             Column('id', Integer, primary_key=True),
             Column('post_title', String(200), nullable=False),
             Column('post_slug', String(200), nullable=False),
             Column('content', Text(), nullable=False),
             Column('published', Boolean(), default=False),
             Column('created_on', DateTime, default=datetime.now),
             Column('updated_on', DateTime, default=datetime.now,  onupdate=datetime.now)
             )

#employee = Table('employees', metadata,
#    Column('id', Integer(), primary_key=True),
#    Column('workday', ARRAY(Integer))
#                 )
##### Реляционные связи
## таблица с пользователями
# один ко многим
user = Table('users', metadata,
    Column('id', Integer(), primary_key=True),
    Column('user', String(200), nullable=False),
)
### почтовые отправления оносящиеся к пользователям

posts = Table('posts', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(),  nullable=False),
    Column('user_id', ForeignKey("users.id")),
    #Column('user_id', Integer(), ForeignKey(user.c.id)), ## Можно использовать вариант с конструктором
)

# один к одному
employees = Table('employees', metadata,
    Column('employee_id', Integer(), primary_key=True), ## первичный ключ
    Column('first_name', String(200), nullable=False),
    Column('last_name', String(200), nullable=False),
    Column('dob', DateTime(), nullable=False),
    Column('designation', String(200), nullable=False),
)

employee_details = Table('employee_details', metadata,
    Column('employee_id', ForeignKey('employees.employee_id'), primary_key=True), ## внешний ключ является первичным
    Column('ssn', String(200), nullable=False),
    Column('salary', String(200), nullable=False),
    Column('blood_group', String(200), nullable=False),
    Column('residential_address', String(200), nullable=False),
    CheckConstraint('salary < 100000', name='salary_check') ## проверка вводимых значений
)

## многий ко многим
#posts = Table('posts', metadata,
#    Column('id', Integer(), primary_key=True),
#    Column('post_title', String(200), nullable=False),
#    Column('post_slug', String(200),  nullable=False),
#    Column('content', Text(),  nullable=False)
#)

tags = Table('tags', metadata,
    Column('id', Integer(), primary_key=True),
    Column('tag', String(200), nullable=False),
    Column('tag_slug', String(200),  nullable=False),
)

post_tags = Table('post_tags', metadata,
    Column('post_id', ForeignKey('posts.id')),
    Column('tag_id', ForeignKey('tags.id'))
)

for t in metadata.tables:
    print(metadata.tables[t])

print('-------------')

for t in metadata.sorted_tables:
    print(t.name)

print(posts.columns)         # вернуть список колонок
print(posts.c)               # как и post.columns
print(posts.foreign_keys)    # возвращает множество, содержащий внешние ключи таблицы
print(posts.primary_key)     # возвращает первичный ключ таблицы
print(posts.metadata)        # получим объект MetaData из таблицы
print(posts.columns.post_title.name)     # возвращает название колонки
print(posts.columns.post_title.type)     # возвращает тип колонки


metadata.create_all(engine)

