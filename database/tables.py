from sqlalchemy import MetaData, Table, Integer, String, Column, Date, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Case(Base):
    __tablename__ = 'CASE'

    number = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    incident_date = Column(Date)
    location = Column(String)
    party_size = Column(Integer)
    referred = Column(String)
    vash_staff = Column(Integer, ForeignKey('STAFF.id_'))
    email = Column(String)
    notes = Column(String)
    mma = Column(String)
    visitor_type = Column(String)

    Staff = relationship('Staff', backref='Case')

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.incident_date} {self.location} {self.major_market_area}'


class Staff(Base):
    __tablename__ = 'STAFF'

    id_ = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    download_location = Column(String)

