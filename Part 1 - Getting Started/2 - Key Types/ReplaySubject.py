from datetime import timedelta
from time import sleep
from rx.subjects import ReplaySubject
from rx.concurrency.immediatescheduler import ImmediateScheduler

lambda_early = lambda x: print("Early:{}".format(x))
lambda_late = lambda x: print("Late: {}".format(x))

subject = ReplaySubject()
subject.subscribe(on_next=lambda_early)
subject.on_next(0)
subject.on_next(1)
subject.subscribe(on_next=lambda_late)
subject.on_next(2)

print("=" * 10)

subject = ReplaySubject(buffer_size=2)
subject.on_next(0)
subject.on_next(1)
subject.on_next(2)
subject.subscribe(on_next=lambda_late)
subject.on_next(3)

print("=" * 10)

subject = ReplaySubject(window=timedelta(milliseconds=150),
                        scheduler=ImmediateScheduler())
subject.on_next(0)
sleep(0.1)
subject.on_next(1)
sleep(0.1)
subject.on_next(2)
subject.subscribe(on_next=lambda_late)
subject.on_next(3)
