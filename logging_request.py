'''
Records the session information to database.
'''


from db_setup import *
import datetime

def logging_request(session_id, request_con):
    '''
    logging_request records the session information to database
    arguments:
        - session_id -> unique session identificator
        - request_con -> access requested by the user 
    '''
    log = request_session.insert()
    log.execute({'session_id': session_id, 'request_con': request_con, 'date': datetime.datetime.now()})
