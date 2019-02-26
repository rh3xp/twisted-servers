#! /usr/bin/env python


from twisted.internet import protocol, reactor


class EchoServer(protocol.Protocol):

    def dataReceived(self, data):
        print(data.decode('ascii'))
        self.transport.write(data)


class EchoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return EchoServer()


reactor.listenTCP(8000, EchoFactory())
reactor.run()
