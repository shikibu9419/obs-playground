import socket
import asyncio
import simpleobsws

host = '127.0.0.1'

# obs
loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host=host, port=4444, password='password', loop=loop)

async def make_request(num):
    await ws.connect()
    data = {'scene-name': f'scene{num}'}
    result = await ws.call('SetCurrentScene', data)
    print(result)
    await ws.disconnect()

# socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, 8888))
socket.listen(2)

while True:
    connection, address = socket.accept()
    print(f"Connection from {address} has been established!")

    # クライアントからデータを受信
    recvline = connection.recv(4096).decode()
    print(recvline)

    try:
        num = int(recvline)
        loop.run_until_complete(make_request(num))
        connection.send(str(num).encode())
    except ValueError as e:
        connection.send('Sent integer.'.encode('utf-8'))

connection.close()
socket.close()
