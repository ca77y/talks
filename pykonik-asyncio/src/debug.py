import asyncio
import logging
import os

os.environ["PYTHONASYNCIODEBUG"] = "1"
logging.basicConfig(level=logging.DEBUG)


@asyncio.coroutine
def bug():
    raise Exception("not consumed")

loop = asyncio.get_event_loop()
asyncio.async(bug())
loop.run_forever()
loop.close()
