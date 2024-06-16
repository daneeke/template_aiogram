from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

from loader import db

router = Router()


@router.message(CommandStart())
async def get_start_command_handler(message: Message):
    user_id = message.from_user.id

    row = await db.fetchone(
        'SELECT name FROM users WHERE id = ?;',
        (user_id,)
    )
    user_name: str = row[0]

    user_profile = f'<a href="tg://user?id={user_id}">{user_name}</a>'
    await message.answer(f'Привет, {user_profile}!')
