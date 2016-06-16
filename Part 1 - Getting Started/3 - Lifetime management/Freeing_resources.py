from rx.core import Disposable

s = Disposable.create(lambda: print("Clean"))
s.dispose()
