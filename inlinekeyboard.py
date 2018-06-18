#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    #keyboard = [[InlineKeyboardButton("Ver Tickets", callback_data='1'),
    #             InlineKeyboardButton("Abrir", callback_data='2')],

    #            [InlineKeyboardButton("Option 3", callback_data='3')]]

    #reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Escriba estas opciones: \n/open Escriba Texto Describiendo el Ticket \n /tickets (Para ver la lista de tickets abiertos)')


def button(bot, update):
    query = update.callback_query

    #bot.edit_message_text(text="Selected option: {}".format(query.data),
    #                      chat_id=query.message.chat_id,
    #                      message_id=query.message.message_id)
    if query.data == '1':
        update.message.reply_text("Los tickes abiertos actualmente son: ")

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, No se reconoce este comando")

def open(bot, update, args):
    query = update.callback_query
    if query.data == '1':
        update.message.reply_text("Use /open y una descripcion del ticket.")
    update.message.reply_text("")

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("612717632:AAHKiLydjhDd1DF7y4DJIyn1gwJbhkhUnmY")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    #updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    #comandos para Tickets MB
    updater.dispatcher.add_handler(CommandHandler('open', open))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
