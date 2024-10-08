from aiogram import F, Router, types

voting = Router()

@voting.callback_quiery(F.data.startswith('vote'))
async def vote_handler(callback_query: types.CallbackQuery) -> None:
    ''' Takes votes, where voted_id is id of the player someone voted for '''
    chat_id, voted_id = str(callback_query.data).split()[1:]
    if callback_query.chat.id == chat_id and db.check_vote(chat_id, callback_query.from_user.id, voted_id):
        callback_query.message.answer(f'{callback_query.from_user.fullname} успешно проголосвал!')
    else:
        callback_query.message.answer(f'Голос не засчитан! {callback_query.from_user.fullname} уже проголосвал!')


async def count_voting(chat_id):
    votes = db.get_votes(chat_id)
