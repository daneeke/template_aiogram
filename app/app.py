from asyncio import run

from handlers import start_handler
from loader import bot, dp, db
from middlewares.register_user import RegisteringUserMiddleware


@dp.shutdown()
async def on_shutdown():
    await db.close()
    print('Telegram-Bot has been closed')


async def main():
    await db.initialize()

    await db.execute(
        '''CREATE TABLE IF NOT EXISTS users(
            id bigint PRIMARY KEY,
            name text NOT NULL
        );
        '''
    )
    
    dp.include_router(start_handler.router)
    dp.message.middleware(RegisteringUserMiddleware())

    print('Telegram-Bot has been launched successfully!')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        ...
