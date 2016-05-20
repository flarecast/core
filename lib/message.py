import pylibmc

class Message():
    current_id = 0

    def __init__(self, event, addr, insistence, sender, msg_id = current_id):
        self.event = event
        self.addr = addr
        self.insistence = insistence
        self.sender = sender
        self.id = msg_id
        if(self.id == Message.current_id):
            Message.current_id += 1

    def full_id(self):
        return str(self.id)+'-'+str(self.sender)

    def has_expired(self):
        return self.event.has_expired

    @classmethod
    def init(cls, host = 'localhost', port = 11211):
        cls.__memcached = pylibmc.Client(['%s:%s' % (host, port)],
                                         binary=True,
                                         behaviors={"tcp_nodelay": True,
                                                    "ketama": True})

    @classmethod
    def register(cls, msg_id, addrs = []):
        reg_addrs = cls.__memcached.get(msg_id)
        saved_addrs = addrs if reg_addrs is None else reg_addrs + addrs
        cls.__memcached.set(msg_id, saved_addrs)

    @classmethod
    def addrs(cls, msg_id):
        return cls.__memcached.get(msg_id)

