from telegram.ext import Updater
from telegram.ext import CommandHandler

import config

updater = Updater(config.token, use_context=True)


def start(update, context):
    #import pdb;pdb.set_trace()
    chat_id=update.effective_chat.id
    
    context.bot.send_message(chat_id,text = 'Hello')



# --------------Command--------------- #

start_command = CommandHandler('start',start)


# -----------------------Dispatcher-----------------------#

updater.dispatcher.add_handler(start_command)





updater.start_polling()
updater.idle()
