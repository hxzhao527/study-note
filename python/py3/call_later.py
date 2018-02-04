#!/usr/bin/python3
# -*-coding:utf8-*-
'''
学习asyncio 之 call_later,
观察 call_later 到底什么时候执行的.
'''
import time
import asyncio
import requests


def block_loop():
    print("In block")
    print(time.time())
    try:
        requests.get("https://www.google.com")
    except:
        pass


def hello_world(loop):
    print(time.time())
    print('Hello World')
    loop.stop()


loop = asyncio.get_event_loop()
loop.set_debug(True)
print(time.time())
# Schedule a call to hello_world()
loop.call_soon(block_loop)
print("call soon")
print(time.time())
loop.call_later(2, hello_world, loop)
print("Register call later.")
print(time.time())
# Blocking call interrupted by loop.stop()
print("Start loop")
loop.run_forever()
loop.close()
'''
result:
1490440460.2086859
call soon
1490440460.2166862
Register call later.
1490440460.2206867
Start loop
In block
1490440460.223687
Executing <Handle block_loop() at e:\project\py3_stu\call_later.py:12 created at e:\project\py3_stu\call_later.py:32> took 22.121 seconds
1490440482.3559527
Hello World
观察可以得到:
hello_world 并不是在注册执行后2秒内运行的,而是等前面的call_soon注册的block_loop返回后才运行,这是因为block_loop在hello_world之前被添加到
loop._ready中,再加上FIFO,所以会看到这个并不准时的延迟执行.
'''
