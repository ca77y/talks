import aiohttp
import asyncio
import random


def read_timeline(idx):
    res = yield from aiohttp.request('get', 'https://github.com/')
    filename = 'github_{}.json'.format(idx)
    with open(filename, 'wb') as fp:
        while True:
            data = yield from res.content.read(10)
            if not data:
                break
            fp.write(data)
            print('written data to {}'.format(filename))
            yield from asyncio.sleep(random.randrange(1,5))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(read_timeline(1), read_timeline(2)))
loop.close()
