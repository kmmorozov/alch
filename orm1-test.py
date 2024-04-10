from sqlalchemy import Table, Index, Integer, String, Column, Text, \
    DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, create_engine
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://dbuser1:123456@192.168.20.29/db1")

class Telsprav(Base):
    __tablename__ = 'telsprav'
    id = Column(Integer)
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    secondname = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    ed = relationship("Extradata")

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )


class Extradata(Base):
    __tablename__ = 'extradata'
    id = Column(Integer, primary_key=True)
    about = Column(String(50), nullable=False)
    user_id = Column(Integer(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['telsprav.id']),
        Index('id', 'user_id'),
    )

Base.metadata.create_all(engine)