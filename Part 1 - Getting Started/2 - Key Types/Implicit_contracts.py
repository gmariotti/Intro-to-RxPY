from rx.subjects import ReplaySubject

subject = ReplaySubject()
subject.subscribe(on_next=print)
subject.on_next(0)
subject.on_completed()
# doesn't print anything after on_completed()
subject.on_next(1)
subject.on_next(2)
