from telegram import ForceReply, Update
from telegram.ext import ContextTypes
from script.response import response, saveuser
import logging
from helpers import load_from_update
from sqlalchemy import text
from database import session
from script.coreapi import *
import os
from dotenv import load_dotenv
load_dotenv()
from .scrapper import *

FE_URL = os.getenv('FE_AUTH_URL')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    data = load_from_update(update)
    await update.message.reply_html(
        rf"Hi {data['user']['first_name']}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    text = """
Menu Bantuan.
/start - Memulai Penggunaan BOT.
/help - Menu Bantuan.
/stats - Statistik Chat Saat Ini.

by ajcc 2023.
    """
    await update.message.reply_text(text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    res = response(load_from_update(update))
    logger.info(msg=res)
    # await update.message.reply_text(res)
    state = update.message.text.lower()
    if state == "@all":
        await all_users(update, context)
    elif state == "@admin":
        await all_admin(update, context)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    data = load_from_update(update)
    sql = text("""
        SELECT
            m.user_id,
            m.name,
            CONCAT('@', m.username) as username,
            (
                SELECT COUNT(*)
                FROM
                    message_logs ml
                WHERE
                    ml.member_id = m.user_id
            ) as stats
        FROM
            members m
        ORDER BY
            stats
        DESC
        LIMIT 10
    """)
    results = session.execute(sql)
    response = "Statistik Jumlah Chat:"
    for i, record in enumerate(results):
        response += f"\n{i+1}. {record[2]} -> {record[3]} chat"
    await update.message.reply_html(
        response,
        reply_markup=ForceReply(selective=True),
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    data = load_from_update(update)
    user = data['user']
    dataLog = await getToken(user['id'], user['username'])
    if dataLog['status'] != 201:
        await update.message.reply_html(
            "error occured or telegram user id has been registered",
            reply_markup=ForceReply(selective=True),
        )
    text = f"""
{dataLog['data']['message']}
{FE_URL}{dataLog['data']['data']['register_token']}
    """
    await context.bot.send_message(
        chat_id=update.message.from_user.id,
        text=text,
        parse_mode='HTML')
    
async def all_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sql = text("""
        SELECT
            CONCAT('@', m.username) as username
        FROM
            members m
        LIMIT 10
    """)
    results = session.execute(sql)
    users = ""
    for res in results:
        users += f" {res[0]}"
    must_delete = await update.message.reply_html(
        text=users,
        reply_markup=ForceReply(selective=True),
    )
    await context.bot.deleteMessage(
        message_id = must_delete.message_id,
        chat_id = update.message.chat_id
    )
    await update.message.reply_html(
        "Pinging all active users",
        reply_markup=ForceReply(selective=True),
    )

async def all_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = await context.bot.get_chat_administrators(update.message.chat_id)
    
    users = ""
    for d in data:
        users += f" @{d.user.username}"
    must_delete = await update.message.reply_html(
        text=users,
        reply_markup=ForceReply(selective=True),
    )
    await context.bot.deleteMessage(
        message_id = must_delete.message_id,
        chat_id = update.message.chat_id
    )
    await update.message.reply_html(
        "Pinging all administrators",
        reply_markup=ForceReply(selective=True),
    )

async def scrap_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cmd = update.message.text.split(" ")
    if len(cmd) >= 2:
        data = await scrap_users(cmd[1])
        for d in data:
            saveuser(d)
        await update.message.reply_html(
            f"Total users scrapped : {len(data)}",
            reply_markup=ForceReply(selective=True),
        )
    else: 
        await update.message.reply_html(
            "Please insert telegram group url",
            reply_markup=ForceReply(selective=True),
        )

async def scrap_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cmd = update.message.text.split(" ")
    if len(cmd) >= 2:
        await update.message.reply_html(
            f"Scrapping Chats Started",
            reply_markup=ForceReply(selective=True),
        )
        data = await scrap_chats(cmd[1])
        await update.message.reply_html(
            f"Success Scrapping Chats count : {data}",
            reply_markup=ForceReply(selective=True),
        )
    else: 
        await update.message.reply_html(
            "Please insert telegram group url",
            reply_markup=ForceReply(selective=True),
        )