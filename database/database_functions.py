from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from database.create_database import DB_PATH
from database import tables
from datetime import datetime

# DB_PATH = 'sqlite:///../report_database.db'
DB_PATH = 'sqlite:///report_database.db'


engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)


def insert_case(data: dict):
    case = tables.Cases(
        first_name=data['first name'],
        last_name=data['last name'],
        incident_date=datetime.strptime(data['incident date'], '%m/%d/%y'),
        party_size=data['party size'],
        referred=data['referred by'],
        vash_staff='bart',
        email='victim@mail.com',
        notes=data['case notes'],
        mma=data.get('mma'),
        visitor_type=data['visitor type'],
    )
    # case.first_name = data['first name']
    # case.last_name = data['last name']
    # case.incident_date = data['incident date']
    session = Session()
    session.merge(case)
    session.commit()


def insert_staff():
    staff = tables.Staff(first_name='bart', last_name='simpson',
                         email='bs@mail.com', download_location='root dir baby')
    session = Session()
    session.merge(staff)
    session.commit()
