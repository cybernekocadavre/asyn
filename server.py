#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    client_address = writer.get_extra_info('socket').getpeername()
    print(f"Получили сообщение: {message} от:  {client_address}")

    print(f"Посылаем: {message}")
    writer.write(data)
    await writer.drain()

    print("Закрываем соединение")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Работаем на: {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())

