from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from data.config import token, DATABASE_PATH
from utils.chdir import chdir
from utils.database import Database

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

chdir(__file__)

db = Database(DATABASE_PATH)
