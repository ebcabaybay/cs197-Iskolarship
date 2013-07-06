from sqlalchemy import *
from database import Base

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message = Column(String(255))

<<<<<<< HEAD
class Persons(Base):
	__tablename__ = 'persons'
	personid = Column(Integer, primary_key=True)
	lastname = Column(String(30))
	firstname = Column(String(30))
	middlename = Column(String(30))
	namesuffix = Column(String(10))
=======
class Student(Base):
    __tablename__ = 'students'
    studentid = Column(Integer, primary_key=True)
    personid = Column(Integer)
    programid = Column(Integer)
    familyincome = Column(Numeric)
    reasonforneedingscholarship = Column(String)

class Person(Base):
    __tablename__ = 'persons'
    personid = Column(Integer, primary_key=True)
    lastname = Column(String(30))
    firstname = Column(String(30))
    middlename = Column(String(30))
    namesuffix = Column(String(30))
    birthday = Column(DateTime))
    sex = Column(Integer)
>>>>>>> 438b1252229ecfad6b02f0c15e2a05aeeb0e821e
