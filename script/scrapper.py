from telethon.sync import TelegramClient
import os
from dotenv import load_dotenv
from .response import logger

load_dotenv()

async def scrap_users(link) -> list:
   data = [] 
   async with TelegramClient(os.getenv('PHONE'), os.getenv('API_ID'), os.getenv('API_HASH')) as client:
      data = await client.get_participants(link)
   return [{"id": d.id, "first_name": d.first_name, "username": d.username} for d in data]


async def scrap_chats(link) -> int:
   data = 0
   async with TelegramClient(os.getenv('PHONE'), os.getenv('API_ID'), os.getenv('API_HASH')) as client:
      async for message in client.iter_messages(link):
         # print(message)
         try:
            logger(message.id, message.message, message.from_id.user_id, message.date)
            data +=1
         except:
            pass
   return data
   # return [{"id": d.id, "first_name": d.first_name, "username": d.username} for d in data]