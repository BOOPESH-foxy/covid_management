from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemyDbconnect

engine = create_engine(sqlalchemyDbconnect.url)
session = sessionmaker(bind=engine)
Session = session()

Base = declarative_base()
class MyTable(Base):
    __tablename__ = 'Authentication'
    Id = Column(Integer, primary_key=True)
    name = Column(String(255))
    isStaff = Column(Integer)
    
row = MyTable(Id = 1004,name='San', isStaff = 0)
Session.add(row)
Base.metadata.create_all(engine)
Session.commit()
print(row)

