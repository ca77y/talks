import asyncio


@asyncio.coroutine
def task1():
    print('task1')

    return 'hello world'


@asyncio.coroutine
def task2():
    print('before task1')

    fut = task1()

    print('after task1')

    text = yield from fut

    print('after yield')
    print(text)


loop = asyncio.get_event_loop()
loop.run_until_complete(task2())
loop.close()
