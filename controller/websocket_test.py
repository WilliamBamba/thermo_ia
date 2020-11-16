import asyncio
import websockets

async def hello():
    uri ='ws://localhost:8000/sensors/exchange_data'
    

    async with websockets.connect(uri) as websocket:
        while True:
            name = input("What's your name? ")

            await websocket.send(name)
            recv = await websocket.recv()
            print(recv)

asyncio.get_event_loop().run_until_complete(hello())