from rx import Observable


def subscribe(observer):
    observer.on_next(1)
    observer.on_next(1)
    observer.on_next(2)
    observer.on_next(3)
    observer.on_next(2)
    observer.on_completed()


print("\n== distinct ==")
values = Observable.create(subscribe)
subscription = values.distinct().subscribe(
    on_next=print,
    on_error=lambda e: print("Error: {}".format(e)),
    on_completed=lambda: print("Completed")
)


def subscribe2(observer):
    observer.on_next("First")
    observer.on_next("Second")
    observer.on_next("Third")
    observer.on_next("Fourth")
    observer.on_next("Fifth")
    observer.on_completed()


print("")
values = Observable.create(subscribe2)
subscription = values.distinct(lambda v: v[0]).subscribe(
    on_next=print,
    on_error=lambda e: print("Error: {}".format(e)),
    on_completed=lambda: print("Completed")
)

print("\n== distinctUntilChanged ==")
values = Observable.create(subscribe)
subscription = values.distinct_until_changed().subscribe(
    on_next=print,
    on_error=lambda e: print("Error: {}".format(e)),
    on_completed=lambda: print("Completed")
)

print("")
values = Observable.create(subscribe2)
subscription = values.distinct_until_changed(lambda v: v[0]).subscribe(
    on_next=print,
    on_error=lambda e: print("Error: {}".format(e)),
    on_completed=lambda: print("Completed")
)
