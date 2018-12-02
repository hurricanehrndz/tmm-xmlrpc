from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from tmm_xmlrpc.tmm import tmm


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
def start_server(tiny_media_manager):
    server = SimpleXMLRPCServer(('0.0.0.0', 8000),
                                requestHandler=RequestHandler)

    server.register_instance(tmm(tiny_media_manager))

    try:
        print('Use Control-C to exit')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
