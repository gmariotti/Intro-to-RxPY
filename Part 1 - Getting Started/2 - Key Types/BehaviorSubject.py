from rx.subjects import BehaviorSubject

subject = BehaviorSubject(0)
subject.on_next(1)
subject.on_next(2)
subject.subscribe(on_next=lambda v: print("Late: {}".format(v)))
subject.on_next(3)

print("=" * 10)

subject = BehaviorSubject(0)
subject.on_next(1)
subject.on_next(2)
subject.on_completed()
subject.subscribe(
    on_next=lambda v: print("Late: {}".format(v)),
    on_error=lambda e: print("Error"),
    on_completed=lambda: print("Completed")
)
