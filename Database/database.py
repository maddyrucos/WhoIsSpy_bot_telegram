from distutils.command.config import config

import sqlalchemy as sq
from sqlalchemy import orm
from models import Base, User, Game
import config

engine = sq.create_engine(f'postgresql+psycopg://{config.USER}:{config.PASSWORD}@localhost/{config.DBNAME}')
engine.connect()
session = orm.Session(bind=engine)
Base.metadata.create_all(bind=engine)

def create_profile(user_id: int, fullname: str, username: str) -> None:
    ''' Tries to add user data into DB (only new users) '''
    try:
        new_user = User(id=user_id, fullname=fullname, username=username)
        session.add(new_user)
        session.commit()
    except sq.exc.IntegrityError:
        print('This user already exists!')
    except Exception as e:
        print(e.with_traceback)


def get_user_json(user_id) -> dict:
    ''' Returns users data in JSON '''
    player = session.get(User, user_id)
    player_json = {
            "name": player.fullname,
            "spy": 0,
            "username": player.username,
    }
    return player_json


def create_game(chat_id: int, user_id: int, word: str) -> int:
    ''' Creates new game '''
    if session.query(Game).filter(Game.status==True, Game.chat_id==chat_id).first():
        return 0
    else:
        player_json = get_user_json(user_id)
        new_game = Game(chat_id=chat_id, players={user_id: player_json}, status=True, word=word)
        session.add(new_game)
        session.commit()
        return 1


def get_players(chat_id: int) -> dict:
    ''' Returns players dict with parameters: id, fullname and role(1 if spy else 0)  '''

    return {}


def add_player(chat_id: int, user_id: int) -> int:
    ''' Adds player to game linked to chat by chat_id '''
    game = session.query(Game).filter(Game.status == True, Game.chat_id == chat_id).first()
    if game:
        print(game.status)
        players = game.players
        player_json = get_user_json(user_id)
        players[user_id] = player_json
        game.players = players
        game.status = False
        print(f'{game.players=}')
        session.commit()
        return 1
    else:
        return 0


def add_word(chat_id: int, word: str) -> int:
    ''' Links word of the game with chat by chat_id '''
    return 0


def add_vote(chat_id: int, voter_id: int, player_id: int) -> int:
    '''
    Adds vote to database.
    voter_id - id of player that pushed the button
    player_id - id of player that gets vote
    '''
    return 0


def get_votes(chat_id: int) -> list:
    ''' Collects list of votes from database '''
    return []

if __name__ == '__main__':
    #create_profile(1234, 'Player1', 'Username')
    #create_profile(3214, 'Player2', 'User')
    #print(create_game(54321, 1234))
    print(add_player(54321,3214))
    session.commit()

    session.close()