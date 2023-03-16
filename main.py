from telegram.ext import *
from response import response
import os
from dotenv import load_dotenv
load_dotenv()

Token = os.getenv('API_KEY')
def start_command(update, context):
    update.message.reply_text("test start")

def help_command(update, context):
    update.message.reply_text("test help")

def handle_message(update, context):
    resp = response(update)
    update.message.reply_text(str(resp))

def error(update, context):
    print(f"error {context.error}")

def main():
    print("Bot Started")
    updater = Updater(Token,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()