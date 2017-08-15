from sqlalchemy import *

db = create_engine('sqlite:///app_connection.db')
db.echo = False
metadata = MetaData(db)

request_session = Table('request_session', metadata,
                Column('request_id', Integer, primary_key = True),
                Column('session_id', String(32)),
                Column('request_con', String(256)),
                Column('date', DateTime),
                sqlite_autoincrement = True)
