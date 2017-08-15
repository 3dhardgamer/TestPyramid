'''
Database structure
'''

from sqlalchemy import *

db = create_engine('sqlite:///app_connection.db')
db.echo = False
metadata = MetaData(db)

# Attributes recorded:
# request_id -> incresing counter for the number of request done to server
# session_id -> unique session identificator
# request_con -> path requested by the user
# date -> date when request action happened
request_session = Table('request_session', metadata,
                Column('request_id', Integer, primary_key = True),
                Column('session_id', String(32)),
                Column('request_con', String(256)),
                Column('date', DateTime),
                sqlite_autoincrement = True)
