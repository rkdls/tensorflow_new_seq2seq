import argparse
import asyncio
import aiohttp

def function1873(arg493):
    var1865 = aiohttp.ClientSession()
    var881 = yield from var1865.request('GET', arg493)
    print(repr(var881))
    var3637 = yield from var881.content.read()
    print(('Downloaded: %s' % len(var3637)))
    var881.close()
    yield from var1865.close()
if (__name__ == '__main__'):
    var627 = argparse.ArgumentParser(description='GET url example')
    var627.add_argument('url', nargs=1, metavar='URL', help='URL to download')
    var627.add_argument('--iocp', default=False, action='store_true', help='Use ProactorEventLoop on Windows')
    var3320 = var627.parse_args()
    if var3320.iocp:
        from asyncio import events, windows_events
        var3481 = windows_events.ProactorEventLoop()
        events.set_event_loop(var3481)
    var519 = asyncio.get_event_loop()
    var519.run_until_complete(function1873(var3320.url[0]))