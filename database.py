def get_players(chat_id: int) -> dict:
    ''' Return players dict with parameters: id, fullname and role(1 if spy else 0)  '''
    return {}


def add_player(chat_id: int, user_id: int, user_name: str) -> int:
    ''' Adds player to game linked to chat by chat_id '''
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