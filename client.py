#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Получили: {data.decode()}")

    print("Закрываем соединение")
    writer.close()
    await writer.wait_closed()

async def main():
    await tcp_echo_client('учебно-научный семинар')

asyncio.run(main())

