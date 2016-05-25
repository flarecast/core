import redis
import pickle

class Message():
    current_id = 0

    def __init__(self, event, addr, insistence, sender, msg_id = None):
        self.event = event
        self.addr = addr
        self.insistence = insistence
        self.sender = sender
        if msg_id is None:
            Message.current_id += 1
            self.id = Message.__build_id(Message.current_id, sender)
        else:
            self.id = msg_id

    @classmethod
    def __build_id(cls, id, sender):
        return str(id) + '-' + str(sender)

    def event_creator(self):
        # TODO: change to event.creator
        return self.sender

    def has_expired(self):
        return self.event.has_expired()

    @classmethod
    def init(cls, host = 'localhost', port = 6379):
        cls.__redis = redis.Redis(host=host, port=port, db=0)
        cls.__redis.flushdb()

    @classmethod
    def register(cls, msg_id, addrs = set()):
        reg_addrs = cls.__get(msg_id)
        saved_addrs = addrs if reg_addrs is None else reg_addrs | addrs
        cls.__set(msg_id, saved_addrs)

    @classmethod
    def addrs(cls, msg_id):
        return cls.__get(msg_id)

    @classmethod
    def ids(cls):
        return {k.decode('utf-8') for k in cls.__redis.keys("*")}

    @classmethod
    def __set(cls, key, val):
        cls.__redis.set(key, cls.__d(val))

    @classmethod
    def __get(cls, key):
        return cls.__l(cls.__redis.get(key))

    @classmethod
    def __l(cls, obj):
        return None if obj is None else pickle.loads(obj)

    @classmethod
    def __d(cls, obj):
        return pickle.dumps(obj)

