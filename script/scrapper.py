from telethon.sync import TelegramClient
import os
from dotenv import load_dotenv

load_dotenv()

async def scrap_users(link) -> list:
   data = [] 
   async with TelegramClient(os.getenv('PHONE'), os.getenv('API_ID'), os.getenv('API_HASH')) as client:
      data = await client.get_participants(link)
   return [{"id": d.id, "first_name": d.first_name, "username": d.username} for d in data]