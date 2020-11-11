import asyncio
import websockets

async def accept(websocket, path):
    while True:
        # クライアントからメッセージ待機
        data = await websocket.recv()
        print("received: " + data)
        # クライアントに送信
        await websocket.send("echo:" + data)

# websocketサーバ
start_server = websockets.serve(accept, "127.0.0.1", 50080)
# 非同期待機
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()