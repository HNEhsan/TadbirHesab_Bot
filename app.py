from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import InputMediaDocument
import config

# Create the Updater and pass it your bot's token.
updater = Updater(config.token, use_context=True)

def start(update, context):
    """Send a message when the command /start is issued."""
    keyboard =[
        [
            InlineKeyboardButton("تمایلی ندارم", callback_data='addname'),
            InlineKeyboardButton("وارد کردن نام", callback_data='noname'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('لطفا نام خودرا واردکنید :', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    chat_id=update.effective_chat.id

    # CallbackQueries need to be answered, even if no notification to the user is needed
    query.answer()

    if query.data == 'noname' :
        return addname(update, context)
    context.bot.sendMessage(chat_id, text = 'لطفا پیام خود را وارد کنید :')

def addname(update, context):
    """Send a message when the command /adname is issued."""
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id, text = 'لطفا نام و پیام خود را وارد کنید :')

def echo(update, context):
    """Echo the user message."""
    name = update.message.text
    op = open('Answer/message.txt', 'a')
    op.write(name+'\n\n\t\t******************************************************************************************************************************************************************\t\t\n\n')
    op.close()
    # reply meesage for save name is complete
    update.message.reply_text('اطلاعات شما با موفقیت ثبت شد.')

def sendfile(update, context):
    """Send a message when the command /sendfile is issued."""
    chat_id = update.effective_chat.id
    # find Password
    password = update.message.text
    password = password.split(' ')
    #import pdb;pdb.set_trace()
    if len(password)-1  == 1 :
        password = password[1]
        # check password 
        if password == config.password :
            op = open('Answer/message.txt', 'rb')
            doc = op.read()
            context.bot.sendDocument(chat_id, doc, filename = 'message.txt',  timeout = 50000)
            op.close()
            return
        context.bot.sendMessage(chat_id, text = 'رمز عبور نادرست است')
        return
    context.bot.sendMessage(chat_id, text = 'رمز عبور را وارد کنید')
    return
# ------------------------Command------------------------ #

start_command = CommandHandler('start',start)
addname_command = CommandHandler('addname', addname)
sendfile_command = CommandHandler('sendfile', sendfile)

# -----------------------Dispatcher-----------------------#
# Get the dispatcher to register handlers

updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(addname_command)
updater.dispatcher.add_handler(sendfile_command)
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

# Start the Bot
updater.start_polling()
#Run the bot until you press Ctrl-C or the process receives SIGINT
updater.idle()











