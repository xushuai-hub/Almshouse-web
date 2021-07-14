import socket

IP = "192.168.0.108"

PORT = 9999
address = (IP, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
            sock.bind(address)
            sock.listen(5)
            print('创建了socket')
        return sock