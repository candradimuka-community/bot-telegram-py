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


async def scrap_chats(link) -> None:
   data = [] 
   async with TelegramClient(os.getenv('PHONE'), os.getenv('API_ID'), os.getenv('API_HASH')) as client:
      async for message in client.iter_messages(link):
         # print(message)
         logger(message.id, message.message, message.from_id.user_id, message.date)
   # return [{"id": d.id, "first_name": d.first_name, "username": d.username} for d in data]