import asyncio
import simpleobsws

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='password', loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.

async def make_request():
    print('---------')
    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    print(result) # Print the raw json output of the GetVersion request
    print('---------')
    await asyncio.sleep(1)
    # data = {'scene':'scene1test_source', 'volume':0.5}
    # result = await ws.call('SetVolume', data) # Make a request with the given data
    result = await ws.call('GetCurrentScene') # We get the current OBS version. More request data is not required
    print(result)
    print('---------')
    data = {'scene-name':'scene1'}
    result = await ws.call('SetCurrentScene', data) # Make a request with the given data
    print(result)
    print('---------')
    await ws.disconnect() # Clean things up by disconnecting. Only really required in a few specific situations, but good practice if you are done making requests or listening to events.

loop.run_until_complete(make_request())
