from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Member(Base):
    __tablename__ = 'members'
    
    user_id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)
    name = Column(String)
    logs = relationship("MessageLogs", backref='member')

    def __init__(self, id, username, name):
        self.user_id = id
        self.username = username
        self.name = name