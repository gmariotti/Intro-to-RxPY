from rx import Observable

values = Observable.range(0, 10)
oddNumbers = values.filter(
    lambda v: v % 2 == 0
).subscribe(
    on_next=print,
    on_error=lambda e: print("Error: {}".format(e)),
    on_completed=lambda: print("Completed")
)
