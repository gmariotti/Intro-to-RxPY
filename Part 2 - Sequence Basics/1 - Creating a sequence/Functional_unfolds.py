from rx import Observable, AnonymousObserver
from time import sleep


def print_observer():
    return AnonymousObserver(
        on_next=lambda v: print("Received: {}".format(v)),
        on_error=lambda e: print("Error: {}".format(e)),
        on_completed=lambda: print("Completed")
    )


print("\n== Observable.range ==")
values = Observable.range(10, 15)
values.subscribe(on_next=print)

print("\n== Observable.interval ==")
values = Observable.interval(1000)
subscription = values.subscribe(print_observer())
sleep(5)
subscription.dispose()

print("\n== Observable.timer ==")
values = Observable.timer(1000)
subscription = values.subscribe(print_observer())
sleep(3)

print("\n== Observable.timer to interval ==")
print("Waits two seconds than starts counting every second")
values = Observable.timer(2000, 1000)
subscription = values.subscribe(print_observer())
sleep(5)
subscription.dispose()
