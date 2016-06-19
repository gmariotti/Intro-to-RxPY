from rx.subjects import AsyncSubject

subject = AsyncSubject()
subject.subscribe(on_next=print)
subject.on_next(0)
subject.on_next(1)
subject.on_next(2)
subject.on_completed()
