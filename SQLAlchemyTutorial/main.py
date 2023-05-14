from sqlalchemy import create_engine, ForeignKey, Column, String, CHAR, Integer
from sqlalchemy.ext.declarative import declarative_base # base class of database
from sqlalchemy.orm import sessionmaker # from Object-Relational Mapping import Sessionmaker, which create a session

Base = declarative_base()

class Person(Base): # inherit from Base class
    # add name to database
    __tablename__ = "people"
    social_security_number = Column("ssn", Integer,primary_key=True)
    first_name = Column("firstname", String)
    last_name = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    
