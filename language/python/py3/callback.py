#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
学习asyncio 之 callback
'''
import aiohttp
import asyncio


def hello_callback(response: aiohttp.ClientResponse):
    '''
    callback
    Just show the url of response.
    '''
    print('Callback ' + str(response.url))
    print("Response Id: {id}".format(id=id(response)))
    # print("After request " + str(response._closed))


async def fetch(session, url, callback):
    '''
    request
    Request url with GET method.
    And call callback later.
    '''
    async with session.get(url) as response:
        session.loop.call_soon(callback, response)
        # await callback(response)
        print('Request ' + url)
        print("Response Id: {id}".format(id=id(response)))
        # print("In request " + str(response._closed))
    # print("Out request " + str(response._closed))


async def fetch2(session, url, callback):
    '''
    request
    Request url with GET method.
    And call callback later.
    '''
    async with session.get(url) as response:
        # session.loop.call_soon(callback, response)
        # await asyncio.sleep(10)
        callback(response)
        print('Request ' + url)
        print("Response Id: {id}".format(id=id(response)))
        # print("In request " + str(response._closed))
    # print("Out request " + str(response._closed))

'''
async def main(loop):
    print('Start')
    async with aiohttp.ClientSession(loop=loop) as session:
        await fetch(session, 'http://python.org')
        await fetch(session, 'https://www.baidu.com')
'''


def main():
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    tasks = [
        asyncio.ensure_future(
            fetch(session, 'http://www.python.org', hello_callback)),
        asyncio.ensure_future(
            fetch2(session, 'https://www.baidu.com', hello_callback)),
    ]
    loop.run_until_complete(asyncio.gather(*tasks))
    session.close()
    loop.close()


if __name__ == '__main__':
    print("Start")
    main()
'''
结果:
Start
Start
Callback https://www.baidu.com
Response Id: 103290992
Request https://www.baidu.com
Response Id: 103290992
Request http://www.python.org
Response Id: 100867504
Callback https://www.python.org/
Response Id: 100867504
hello_callback 在 fetch 返回后执行,
'''
