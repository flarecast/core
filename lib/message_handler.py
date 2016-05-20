# TODO: Change _singleton to __singleton
from connection_plugin import ConnectionPlugin
from message import Message
import threading

def on_message(f):
    def callback(*args):
        from event_processor import EventProcessor
        msg = f(*args)
        EventProcessor.handle_message(msg.event)
        MessageHandler._singleton.emit_event(msg.event, msg.sender, msg.id)

    return callback

class MessageHandler():
    _singleton = None

    # Singleton Pattern implementation
    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super(MessageHandler, cls).__new__(cls)
        return cls._singleton

    def __init__(self):
        self.processed_messages = []
        self.plugin = ConnectionPlugin.active_plugin()
        self.plugin.start()

    def broadcast(self, msg):
        print(self.plugin.__class__.__name__)
        if( self.__process_message(msg) ):
            self.plugin.broadcast(msg)
            self.__clear_messages()

    @staticmethod
    def __insistance(lifetime):
        # TODO: find a better formula for this
        return 0.3 * lifetime

    @staticmethod
    def __was_processed(msgs, msg):
        for m in msgs:
            if m.full_id() == msg.full_id():
                return True

        return False

    def __process_message(self, msg):
        b = not MessageHandler.__was_processed(self.processed_messages, msg)
        if b: self.processed_messages.append(msg)
        return b

    def __clear_messages(self):
        self.processed_messages = [m for m in self.processed_messages if not m.has_expired()] # ily Python

    def emit_event(self, event, sender = None, msg_id = None):
        addr = self.plugin.address()
        insist = MessageHandler.__insistance(event.lifetime)
        if sender is None: sender = addr
        if msg_id is not None: 
            msg = Message(event, addr, insist, sender, msg_id)
        else:
            msg = Message(event, addr, insist, sender)
        self.broadcast(msg)

