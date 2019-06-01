#!/usr/bin/python3
# -*-coding:utf8-*-
'''
学习asyncio 之 call_soon,
观察 call_soon 到底什么时候执行的.
'''
import time
import asyncio


def hello_world(loop):
    print('Hello World')
    loop.stop()


loop = asyncio.get_event_loop()
loop.set_debug(True)
print(time.time())
# Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)
hello_world(loop)
print(time.time())
# Blocking call interrupted by loop.stop()
loop.run_forever()
print(time.time())
loop.close()
'''
result:
hello_world(loop)
    1490256568.8851044
    Hello World
    1490256568.8861046
    1490256568.8871045
loop.call_soon(hello_world, loop)
    1490256543.6436608
    1490256543.6516612
    Hello World
    1490256543.6526613
可以看出call_soon是在loop.run_forever()之后才运行,即事件循环开始之后才有call_soon
而call_soon是FIFO, 仍存在阻塞的情况.
'''
