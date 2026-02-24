import asyncio
import websockets
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print(f"Получено сообщение: {message}")
        for i in range(5):
            response = f"Сервер получил: {message} (ответ {i+1})"
            await websocket.send(response)
            await asyncio.sleep(1)

async def main():
    async with serve(echo, "localhost", 8765):
        print("Websocket сервер запущен на ws://localhost:8765")
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())
