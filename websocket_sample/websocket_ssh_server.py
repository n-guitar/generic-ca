# pip install websockets==8.1
import asyncio
import websockets

# paramiko==2.7.2
from paramiko import SSHClient, AutoAddPolicy
import time

# ToDo backspace対応してない
async def accept(websocket, path):
    dataline = ""

    #  ssh
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname='ip address',username='user',password='password',port=22)
    channel = client.invoke_shell()
    while not channel.recv_ready():
        time.sleep(0.1)
    buff = ''
    resp = channel.recv(9999).decode('utf-8')
    buff += resp
    print(resp)
    # login message
    dataline = resp

    def send_command(cmd):
        buff = ''
        while not buff.endswith(']# '):
            channel.send(cmd + '\n')
            resp = channel.recv(9999).decode('utf-8')
            buff += resp
            return str(resp)

    while True:
        # クライアントからメッセージ待機
        data = await websocket.recv()

        if data == "send":
            # クライアントに送信
            dataline = send_command(dataline)
            await websocket.send(dataline)
            data = ""
            dataline = ""
        dataline = dataline + data
        print("received: " + data)
        print("dataline: " + dataline)

# websocketサーバ
start_server = websockets.serve(accept, "127.0.0.1", 50080)
# 非同期待機
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()