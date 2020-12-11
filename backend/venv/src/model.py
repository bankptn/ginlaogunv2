import sqlalchemy as sa
from sqlalchemy import Column , ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ACCOUNT(Base):
    __tablename__ = 'ACCOUNT'
    ssn = Column('ssn', sa.String(13) ,primary_key=True)
    fname = Column('fname', sa.String(20) )
    lname = Column('lname', sa.String(20) )
    username = Column('username', sa.String(15) )
    password = Column('password', sa.String(15) )
    address = Column('address', sa.String(50) )
    email = Column('email', sa.String(30) )
    phoneNumber = Column('phoneNumber', sa.String(15) )
    birthDay = Column('birthDay', sa.String(15) )

class RESTAURANT(Base):
    __tablename__ = 'RESTAURANT'
    rid = Column('rid', sa.String(10) ,primary_key=True)
    detail = Column('detail', sa.String(20) )
    promotion = Column('promotion', sa.String(20) )
    tableRemain = Column('tableRemain', sa.Integer() )
    name = Column('name', sa.String(50) )

class RESTAURANT_ADDRESS(Base):
    __tablename__ = 'RESTAURANT_ADDRESS'
    rid = Column('rid', ForeignKey('RESTAURANT.rid') ,primary_key=True)
    street = Column('street', sa.String(30) )
    province = Column('province', sa.String(30) )
    country = Column('country', sa.String(30) )
    zip = Column('zip', sa.String(5) )

class RESERVATION(Base):
    __tablename__ = 'RESERVATION'
    ssn = Column('ssn', ForeignKey('ACCOUNT.ssn') ,primary_key=True)
    rid = Column('rid', ForeignKey('RESTAURANT.rid') ,primary_key=True)
    createDate = Column('createDate', sa.String(15) )
    tableAmount = Column('tableAmount', sa.Integer() )
    detail = Column('detail', sa.String(50) )
