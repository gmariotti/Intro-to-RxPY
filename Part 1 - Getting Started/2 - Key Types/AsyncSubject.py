from rx.subjects import AsyncSubject

subject = AsyncSubject()
subject.subscribe(on_next=lambda v: print(v))
subject.on_next(0)
subject.on_next(1)
subject.on_next(2)
subject.on_completed()
