from rx import Observable, AnonymousObserver
import time


def print_observer():
    return AnonymousObserver(
        on_next=lambda v: print("Received {}".format(v)),
        on_error=lambda e: print("Error: {}".format(e)),
        on_completed=lambda: print("Completed")
    )


# in RxPY just accepts a single value, and not a list as in RxJava
print("\n== Observable.just ==")
values = Observable.just(["one", "two", "three"])
subscription = values.subscribe(print_observer())

print("\n== Observable.empty ==")
values = Observable.empty()
subscription = values.subscribe(print_observer())

print("\n== Observable.never ==")
values = Observable.never()
subscription = values.subscribe(print_observer())

# is the error operator for RxPY
print("\n== Observable.throw ==")
values = Observable.throw(Exception("Oops"))
subscription = values.subscribe(print_observer())

print("\n== Observable.defer ==")
now = Observable.just(time.clock())
now.subscribe(on_next=print)
time.sleep(1)
now.subscribe(on_next=print)

now = Observable.defer(lambda: Observable.just(time.clock()))
now.subscribe(on_next=print)
time.sleep(1)
now.subscribe(on_next=print)

print("\n== Observable.create ==")


def subscribe(observer):
    observer.on_next("Hello")
    observer.on_completed()


values = Observable.create(subscribe)
subscription = values.subscribe(print_observer())
