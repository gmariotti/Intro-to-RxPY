from rx.subjects import ReplaySubject

values = ReplaySubject()
subscription = values.subscribe(
    on_next=print,
    on_error=print,
    on_completed=lambda: print("Done")
)
values.on_next(0)
values.on_next(1)
subscription.dispose()
values.on_next(2)

print("=" * 10)

values = ReplaySubject()
subscription1 = values.subscribe(on_next=lambda v: print("First {}".format(v)))
subscription2 = values.subscribe(on_next=lambda v: print("Second {}".format(v)))
values.on_next(0)
values.on_next(1)
subscription1.dispose()
print("Unsubscribed first")
values.on_next(2)
