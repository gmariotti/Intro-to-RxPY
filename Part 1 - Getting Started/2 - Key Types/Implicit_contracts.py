from rx.subjects import ReplaySubject

subject = ReplaySubject()
subject.subscribe(lambda v: print(v))
subject.on_next(0)
subject.on_completed()
# doesn't print anything after on_completed()
subject.on_next(1)
subject.on_next(2)
