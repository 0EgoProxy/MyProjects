from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def suka():
    greeting = KeyboardButton('Привет! https://t.me/c/1376586712/4')
    greet_kb = ReplyKeyboardMarkup()
    greet_kb.add(greeting)
