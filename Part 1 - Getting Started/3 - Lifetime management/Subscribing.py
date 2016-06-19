from rx.subjects import ReplaySubject

subject = ReplaySubject()
subject.subscribe(
    on_next=print,
    on_error=print
)
subject.on_next(0)
subject.on_error(Exception("Oops"))
