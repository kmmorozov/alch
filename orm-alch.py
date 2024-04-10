from sqlalchemy import (create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, Text, ForeignKeyConstraint, Boolean, PrimaryKeyConstraint,
                        UniqueConstraint, Index)
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from datetime import datetime
Base = declarative_base()
engine = create_engine("postgresql+psycopg2://dbuser1:123456@192.168.20.29/db1")

class Telsprav(Base):
    __tablename__ = 'telsprav'
    id = Column(Integer)
    abname = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    about = Column(Text, nullable=True)
    __table_args__ = (
        PrimaryKeyConstraint('id', name='ts_pk'),
        UniqueConstraint('phone')
         )



class Extradata(Base):
    __tablename__ = 'extradata'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), nullable=False)
    age = Column(Integer(), nullable=True)
    sex = Column(Boolean, nullable=True)
    note = Column(Text, nullable=True)
    __table_args__ = (
        ForeignKeyConstraint('user_id', 'ts_pk')
    )

Base.metadata.create_all(engine)