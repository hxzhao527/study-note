#!/usr/bin/python3
# -*-coding:utf8-*-

'''
学习asyncio 之 await
观察 await 到底做了啥
'''


import asyncio
import asyncio.futures as futures


async def with_block():
    await asyncio.sleep(1.0)
    print("haha")
    return 1


def fake_with_block(loop):
    future = loop.create_future()
    future._loop.call_later(
        1.0, futures._set_result_unless_cancelled, future, None)

    def _await():
        while not future.done():
            yield future
    yield from _await()
    future._loop.stop()
    print("haha")
    return 1


async def test_wait(loop):
    ff = fake_with_block(loop)
    try:
        ff.send(None)
    except StopIteration as exc:
        print(exc.value)
    await asyncio.sleep(1.0)
    try:
        ff.send(None)
    except StopIteration as exc:
        print(exc.value)
    loop.stop()
loop = asyncio.get_event_loop()
loop.run_until_complete(test_wait(loop))
loop.close()
