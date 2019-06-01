#!/usr/bin/python3
# -*-coding:utf8-*-
'''
学习asyncio 之 call_soon,
观察 call_soon 阻塞循环
'''
import time
import requests
import asyncio


def hello_world1(loop):
    print(time.time())
    requests.get("https://www.google.com")
    print("In one")


def hello_world2(loop):
    print(time.time())
    print('In two')
    loop.stop()


loop = asyncio.get_event_loop()
loop.set_debug(True)
print(time.time())
# Schedule a call to hello_world()
loop.call_soon(hello_world1, loop)
loop.call_soon(hello_world2, loop)
print(time.time())
# Blocking call interrupted by loop.stop()
loop.run_forever()
print(time.time())
loop.close()
'''
result:
'''
