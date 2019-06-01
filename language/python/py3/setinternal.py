#!/usr/bin/python3
# -*-coding:utf8-*-
'''
学习asyncio 之 call_later
'''
import asyncio


def fff():
    print("午时已到")


def setInternal(time, func, loop=None):
    '''
    @:param time internal between each call
    @:param func which function to call, can use functools.partial() to bind argument
    @:param loop which loop to run this
    '''
    async def _run():
        while True:
            func()
            await asyncio.sleep(time)
    return asyncio.ensure_future(_run(), loop=loop)


print("Start")
loop = asyncio.get_event_loop()
task = setInternal(3, fff, loop)
loop.call_later(10, task.cancel)
try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
loop.close()
print("END")
'''
结果:
Start
午时已到
午时已到
午时已到
午时已到
END
??为什么输出四个,不应该是10/3 = 3 个吗?
task.cancel 只取消之后的调用,已开始的不会中止,所以有余数的,都多一次调用.
公式: 调用次数 = math.ceil(总时间/间隔)
'''
