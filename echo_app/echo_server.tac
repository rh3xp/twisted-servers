import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from twisted.application import internet, service
from server import EchoFactory


application = service.Application("Echo")
echoService = internet.TCPServer(8000, EchoFactory())
echoService.setServiceParent(application)

