import asyncio

async def execute(x):
    print('Number',x)
    return x

coroution=execute(1)
print('Coroutine',coroution)
print('After calling execute')
loop=asyncio.get_event_loop()
task = loop.create_task(coroution)
print('Task:',task)
loop.run_until_complete(task)
print('Task:',task)
print('After calling execute')