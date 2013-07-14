from sqlalchemy import *
from database import Base

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message = Column(String(255))

class Students(Base):
    __tablename__ = 'students'
    studentid = Column(Integer, primary_key=True)
    personid = Column(Integer)
    programid = Column(Integer)
    familyincome = Column(Numeric)
    reasonforneedingscholarship = Column(String)

class Persons(Base):
    __tablename__ = 'persons'
    personid = Column(Integer, primary_key=True)
    lastname = Column(String(30))
    firstname = Column(String(30))
    middlename = Column(String(30))
    namesuffix = Column(String(30))
    birthday = Column(DateTime)
    sex = Column(Integer)
    
class Scholarships(Base):
		__tablename__ = 'scholarships'
		scholarshipid = Column(Integer, primary_key=True)
		title = Column(String(50))
		description = Column(String(50))
		program = Column(String(50))
		gender = Column(String(1))
		yearlv = Column(String(50))
		maxincome = Column(Integer)
		filepath = Column(String(100))
