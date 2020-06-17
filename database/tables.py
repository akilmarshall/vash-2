from sqlalchemy import MetaData, Table, Integer, String, Column, Date, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cases(Base):
    __tablename__ = 'CASES'

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

    Staff = relationship('Staff', backref='Cases')

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.incident_date} {self.location} {self.major_market_area}'


class Staff(Base):
    __tablename__ = 'STAFF'

    id_ = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    download_location = Column(String)


if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    DB_PATH = 'sqlite:///report_database.db'
    engine = create_engine(DB_PATH)
    Session = sessionmaker()
    session = Session()
    staff = Staff(first_name='fname', last_name='lname',
                  email='mail', download_location='/home/akil/downloads')
    session.merge(staff)
    session.commit()
