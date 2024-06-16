from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Awaitable, Callable

from loader import db
from utils.escape import escape


class RegisteringUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        message: Message,
        data: dict[str, Any]
    ) -> Awaitable[Any]:
        if not message.from_user.is_bot:
            user_id = message.from_user.id
            user_name = await escape(message.from_user.first_name)

            row = await db.fetchone(
                'SELECT id FROM users WHERE id = ?;',
                (user_id,)
            )
            
            if row is None:
                await db.execute(
                    'INSERT INTO users(id, name) VALUES(?, ?);',
                    (user_id, user_name)
                )
            else:
                await db.execute(
                    'UPDATE users SET name = ? WHERE id = ?;',
                    (user_name, user_id)
                )
        
        result = await handler(message, data)
        return result
