from rx.subjects import ReplaySubject

subject = ReplaySubject()
subject.subscribe(
    on_next=lambda v: print(v),
    on_error=lambda e: print(e)
)
subject.on_next(0)
subject.on_error(Exception("Oops"))
