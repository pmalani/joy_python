import asyncio

def hello_world():
    val = yield "hello"
    print(val)
    yield "world"

h1 = hello_world()
print(h1)
print(next(h1))
print(next(h1))

h2 = hello_world()
print(h2)
print(next(h2))
# send joy
print(h2.send('joy'))

async def hello():
    print("hello")
    await asyncio.sleep(1)
    print("world")

h3 = hello()
print(h3)
asyncio.run(h3)
