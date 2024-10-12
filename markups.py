from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config

ask_group = InlineKeyboardButton(text='Пригласить в группу', url=f'https://t.me/{config.BOT_LINK}?startgroup=true')
start = InlineKeyboardMarkup(inline_keyboard=[[ask_group]])

def create_voting(chat_id: int, players: list):
    ''' Players vote by buttons. Button has callback with chat id and player id '''
    builder = InlineKeyboardBuilder()
    for player in players:
        player_btn = InlineKeyboardButton(player['name'], callback_data=f'vote_{chat_id}_{player["id"]}')
        builder.row(player_btn)

    return builder.as_markup()