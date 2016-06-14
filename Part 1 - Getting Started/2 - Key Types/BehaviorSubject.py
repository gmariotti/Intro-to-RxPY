from rx.subjects import BehaviorSubject

subject = BehaviorSubject(0)
subject.on_next(1)
subject.on_next(2)
subject.subscribe(on_next=lambda x: print("Late: {}".format(x)))
subject.on_next(3)

print("=" * 10)

subject = BehaviorSubject(0)
subject.on_next(1)
subject.on_next(2)
subject.on_completed()
subject.subscribe(
    on_next=lambda x: print("Late: {}".format(x)),
    on_error=lambda x: print("Error"),
    on_completed=lambda: print("Completed")
)
