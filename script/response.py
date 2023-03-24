from database import engine
from models.message_logs import MessageLogs
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

def logger(id, message) -> None:
    try:
        data = MessageLogs(id, message, datetime.now())
        session.add(data)
        session.commit()
    except Exception as e:
        print("ERROR : ", str(e))
        session.rollback()


def response(input_text) -> str:
    logger(input_text['message_id'], input_text)
    return str(input_text)