import asyncio
from aiosqlite import connect

@lambda x: asyncio.run(x())
async def hello_world():
    # example of async context manager
    async with connect(':memory:') as con:
        cur = await con.execute('select * from (values ("hello"), ("world"))')
        # example of async for
        async for row in cur:
            print(f'{row = }')