from twisted.internet.defer import Deferred


def callback_func(result):
    print(result)

def errback_func(failure):
    print(failure)


d = Deferred()
d.addCallback(callback_func)
#d.callback("Triggered the callback")

d.addErrback(errback_func)
#d.addCallbacks(callback_func, errback_func)
d.errback("Error".encode("utf-8"))
