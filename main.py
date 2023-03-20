from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from telegram.ext import *
from script.response import response
import os
from dotenv import load_dotenv
from sys import exit
import time
load_dotenv()
# for bot command
Token = os.getenv('API_KEY')
updater = Updater(Token,use_context=True)
def start_command(update, context):
    update.message.reply_text("Welcome")

def help_command(update, context):
    update.message.reply_text("help command here")

def handle_message(update, context):
    resp = response(update)
    update.message.reply_text(resp)

def error(update, context):
    print(f"error {context.error}")

def main():
    print("Bot Started")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    start()

def start():
    updater.start_polling()
    updater.idle()

def shutdown():
    updater.stop()
    updater.is_idle = False
    print("success shutdown ")
    # main()

def alert():
    print("please restart server to see the change")

# for observer event
def on_created(event):
    print(f"{event.src_path} has been created!")
    alert()

def on_deleted(event):
    print(f"{event.src_path} has been deleted!")
    alert()

def on_modified(event):
    print(f"{event.src_path} has been modified")
    alert()
    # shutdown()

def on_moved(event): 
    print(f"{event.src_path} moving to {event.dest_path}")
    alert()


if __name__ == "__main__":
    patterns = ["*.py"]  
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified 
    my_event_handler.on_moved = on_moved
    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
        main()
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join() 