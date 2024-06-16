from aiosqlite import connect, Connection
from asyncio import Lock
from typing import Any, Optional


class Database:
    def __init__(self, path: str):
        self.path = path

        self.lock = Lock()

        self.connection: (Connection | None) = None
    
    async def initialize(self):
        if self.connection is None:
            self.connection = await connect(self.path)
    
    async def execute(self, sql: str, parameters: Optional[tuple[Any] | None] = None):
        async with self.lock:
            await self.connection.execute(sql, parameters)
            await self.connection.commit()
    
    async def executemany(self, sql: str, parameters: Optional[list[tuple[Any]] | None] = None):
        async with self.lock:
            await self.connection.execute(sql, parameters)
            await self.connection.commit()
    
    async def fetchone(self, sql: str, parameters: Optional[tuple[Any] | None] = None) -> tuple[Any]:
        async with self.lock:
            cursor = await self.connection.execute(sql, parameters)
            row = await cursor.fetchone()
            return row
    
    async def fetchall(self, sql: str, parameters: Optional[tuple[Any] | None] = None) -> tuple[Any]:
        async with self.lock:
            cursor = await self.connection.execute(sql, parameters)
            rows = await cursor.fetchall()
            return rows
    
    async def close(self):
        if self.connection is not None:
            await self.connection.close()
            self.connection = None
