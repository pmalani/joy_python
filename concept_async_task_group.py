import asyncio
from datetime import datetime
from asyncio import sleep as aio_sleep, TaskGroup
from asyncio import run as aio_run

def second():
    return datetime.now().second

async def produce(value):
    await aio_sleep(1)
    return f'hello {value}'

async def produce_hellos():
    print(second())
    print(second(), await produce('world'))
    print(second(), await produce('python'))

aio_run(produce_hellos())

async def gather_hellos():
    print(second())
    print(second(), await asyncio.gather(produce('world'), produce('python')))

aio_run(gather_hellos())

async def task_hellos():
    print(second())
    async with TaskGroup() as tg:
        task1 = tg.create_task(produce('world'))
        task2 = tg.create_task(produce('python'))
    print(second(), task1.result())
    print(second(), task2.result())

aio_run(task_hellos())
