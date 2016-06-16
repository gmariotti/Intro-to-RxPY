from rx.subjects import ReplaySubject

values = ReplaySubject()
subscription1 = values.subscribe(
    on_next=lambda v: print("First: {}".format(v)),
    on_error=lambda e: print("First: {}".format(e)),
    on_completed=lambda: print("Completed")
)
values.on_next(0)
values.on_next(1)
values.on_completed()
values.on_next(2)
