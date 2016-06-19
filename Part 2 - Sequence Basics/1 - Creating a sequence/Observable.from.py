from rx import Observable, AnonymousObserver
import asyncio


def print_observer():
    return AnonymousObserver(
        on_next=lambda v: print("Received: {}".format(v)),
        on_error=lambda e: print("Error: {}".format(e)),
        on_completed=lambda: print("Completed")
    )


@asyncio.coroutine
def future_task(future):
    print("Test future")
    yield from asyncio.sleep(2)
    future.set_result(21)


print("\n== Observable.from ==")
loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(future_task(future))
values = Observable.from_future(future)
values.subscribe(print_observer())
loop.run_until_complete(future)

print("\n== Observable.from ==")
list = [1, 2, 3]
# other aliases are from_list and from_iterable
values = Observable.from_(list)
values.subscribe(print_observer())
