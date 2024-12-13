import socket


class nt_conexxion:
    def __init__(self):
        self.dns = "8.8.8.8"
        self.puerto = 53

    def internet_connection(self):
        try:
            socket.create_connection((self.dns, self.puerto))
            return True
        except OSError:
            return False
