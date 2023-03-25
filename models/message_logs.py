from sqlalchemy import Column, Integer, JSON, DateTime, ForeignKey
from database import Base

class MessageLogs(Base):
    __tablename__ = 'message_logs'
    
    message_id = Column(Integer, primary_key = True)
    message_data = Column(JSON)
    created_at = Column(DateTime)
    member_id = Column(Integer, ForeignKey("members.user_id"))

    def __init__(self, id, message, time):
        self.message_id = id
        self.message_data = message
        self.created_at = time