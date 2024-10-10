from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters.command import Command
from aiogram.filters import CommandStart

from Database import database as db
import markups as mks
import asyncio
import logging
import voting
import config
import random
import time


bot = Bot(config.BOT_TOKEN)

dp = Dispatcher()
router = Router()
dp.include_router(router)
dp.include_router(voting.voting)

@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    if message.chat.type == 'private':
        ''' If the command sent into DM, bot asks to invite him into group '''
        await message.answer('Welcome!', reply_markup = mks.start)
    elif message.chat.type == 'group':
        ''' If the command sent into group, bot sends the rules '''
        await message.answer('smth')
    else:
        logging.ERROR(message.chat.type)
        await message.answer('Error')


@router.message(Command('join'))
async def command_join_handler(message: types.Message) -> None:
    if message.chat.type == 'private':
        ''' If the command sent into DM, bot says that command is only available in groups '''
        await message.answer('Команда доступна только в группах!', reply_markup = mks.start)
    elif message.chat.type == 'group':
        ''' If the command sent into group, bot adds player into db and sends list of players '''
        db.add_player(message.chat.id, message.from_user.id, message.from_user.fullname)
        players = db.get_players(message.chat.id)
        players_str = '\n'.join([str(player['name']) for player in players])
        answer_text = ( 'Вы успешно присоединились к игре!\n'
                        'Список игроков:\n' + players_str + '\n\nДля начала раунда нажмите /play')

        await message.answer(answer_text)
    else:
        logging.ERROR(message.chat.type)
        await message.answer('Error')


@router.message(Command('play'))
async def command_play_handler(message: types.Message) -> None:
    players = db.get_players(message.chat.id)

    ''' Chooses random word from list of words and register it into database'''
    words = ['Больница', 'Кафе', 'Ресторан']
    words_str = '\n'.join([str(word) for word in words])
    word = random.choice(words)
    db.add_word(message.chat.id, word)

    ''' Every player gets message depends on his role '''
    for player in players:
        if not player['spy']:
            await bot.send_message(player['id'], f'Секретное слово: {word}')
        else:
            await bot.send_message(player['id'], 'Ты шпион')

    ''' Round message would be edited according the timer '''
    timer = 600
    message_timer = await message.answer('Раунд начался!\nСписок слов:\n' + words_str +
                                         f'\n\nУ вас осталось {timer} секунд, чтобы найти шпиона')
    for sec in range(timer-1, 0, -1):
        await message_timer.edit_message('Раунд начался!\nСписок слов:\n' + words_str +
                                         f'\n\nУ вас осталось {sec} секунд, чтобы найти шпиона')
        time.sleep(1)

    await bot.send_message(message.chat.id, 'Время вышло! Голосование за шпиона ', reply_markup=mks.voting)

async def run_bot():
    bot.run()


if __name__ == "__main__":
    asyncio.run(run_bot())