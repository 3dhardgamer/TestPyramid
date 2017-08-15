from db_setup import *
import datetime

def logging_request(session_id, request_con):
    log = request_session.insert()
    log.execute({'session_id': session_id, 'request_con': request_con, 'date': datetime.datetime.now()})
