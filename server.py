from http.server import HTTPServer,BaseHTTPRequestHandler
from datetime import datetime

class GMBotHandler(BaseHTTPRequestHandler):
    def __init__(self,msg_dump_dir,*args):
        self.msg_dump_dir=msg_dump_dir
        BaseHTTPRequestHandler.__init__(self,*args)
        return

    def do_POST(self):
        if self.headers.get('User-Agent')!='GroupMeBotNotifier/1.0':
            return
        self.send_response(200)
        self.end_headers()
        print(self.client_address)
        message=self.rfile.read(int(self.headers.get('content-length')))
        print(self.headers.items())
        #Need to get this into the class
        #msg_dump_dir='/var/bot0msg'
        #Note that this will miss multiple messages per second
        with open(self.msg_dump_dir+'msg_'+datetime.now().strftime('%Y-%m-%d_%H:%M:%S'),'wb') as out:
            #with open(msg_dump_dir+'msg_'+datetime.now().strftime('%Y-%m-%d_%H:%M:%S'),'w') as out:
            out.write(message)
        return

class GMBotServer:
    def __init__(self,port,msg_dump_dir):
        def handler(*args):
            GMBotHandler(msg_dump_dir,*args)
        server = HTTPServer(('',port),handler)
        server.serve_forever()
