import os

from dotenv import load_dotenv
import logging

load_dotenv()

""" You need to create .env file and put TOKEN there, or just put TOKEN instead of os.getenv """
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_LINK = 'WhoIsSpyGameBot' # Replace link with your bot's link

DATABASE = 'postgresql+psycopg' # You can change it according to sqlalchemy rules

if DATABASE=='postgresql+psycopg':
    """ Change parameters according your PostgreSQL setup """
    USER = 'postgres'
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DBIP = 'localhost'
    DBNAME = 'postgres'

logging.basicConfig(
    filename='logs.txt',
    filemode='a',
    level=0,
)