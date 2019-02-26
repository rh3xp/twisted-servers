#! /usr/bin/env python


from twisted.internet import protocol, reactor


class EchoClient(protocol.Protocol):

    def connectionMade(self):
        request = "Hello World"
        self.transport.write(request.encode("utf-8"))


    def dataReceived(self, data):
        print(data)
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        reactor.stop()


reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()
