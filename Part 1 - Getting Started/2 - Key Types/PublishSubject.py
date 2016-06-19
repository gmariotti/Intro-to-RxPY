from rx.subjects import Subject

# In RxPY Subject instead of PublishSubject as in RxJava
subject = Subject()
subject.on_next(1)
subject.subscribe(on_next=print)
subject.on_next(2)
subject.on_next(3)
subject.on_next(4)
