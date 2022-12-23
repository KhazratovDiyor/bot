from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, Dispatcher, CommandHandler, callbackcontext
from telegram.update import Update
from settings import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context:callbackcontext):
    update.message.reply_text('SAlom')

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()