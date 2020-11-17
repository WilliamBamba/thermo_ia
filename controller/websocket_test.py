import asyncio
import websockets

async def hello():
    uri ='ws://localhost:8000/sensors/exchange_data'
    

    async with websockets.connect(uri) as websocket:
        while True:
            temp = input("temperature: ")
            data = {'temperature': int(temp)}
            

            await websocket.send(str(data))
            recv = await websocket.recv()
            print(recv)

asyncio.get_event_loop().run_until_complete(hello())