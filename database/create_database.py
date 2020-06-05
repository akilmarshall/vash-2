from sqlalchemy import create_engine
import tables

DB_PATH = 'sqlite:///../report_database.db'
engine = create_engine(DB_PATH)
# Foreign keys are disabled by default in SQLite
engine.execute('pragma foreign_keys=on')

if __name__ == '__main__':
    tables.Base.metadata.create_all(engine)
