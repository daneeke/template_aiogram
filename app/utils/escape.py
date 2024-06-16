from asyncio import get_event_loop
from html import escape as _esc
from html import unescape


async def escape(text: str, _un: bool = False):
    loop = get_event_loop()

    if not _un:
        result = await loop.run_in_executor(None, _esc, text)
    else:
        result = await loop.run_in_executor(None, unescape, text)
    return result
