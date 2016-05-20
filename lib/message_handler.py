from connection_plugin import ConnectionPlugin
from message import Message
import threading
import time

def on_message(f):
    handler = MessageHandler.__singleton
    def callback(*args):
        from event_processor import EventProcessor
        msg = f(*args)

        if(handler.__valid_message(msg)):
            EventProcessor.handle_message(msg.event)
            handler.emit_event(msg.event, msg.sender, msg.id)
        else:
            # Register the sender of the message
            # in case multiple people are sending us the same message
            # that way we won't send to them
            Message.register(msg.id, {msg.sender})

    return callback

class MessageHandler():
    __singleton = None
    REMOVAL_INTERVAL = 1800

    # Singleton Pattern implementation
    def __new__(cls, *args, **kwargs):
        if cls.__singleton is None:
            cls.__singleton = super(MessageHandler, cls).__new__(cls)
        return cls.__singleton

    def __init__(self):
        self.plugin = ConnectionPlugin.active_plugin()
        self.plugin.start()

    def broadcast(self, msg):
        # TODO: check if this print is needed
        print(self.plugin.__class__.__name__)

        Message.register(msg.id, [msg.event_creator, msg.sender])
        self.plugin.broadcast(msg)

    def emit_event(self, event, sender = None, msg_id = None):
        addr = self.plugin.address()
        insist = MessageHandler.__insistence(event.lifetime)
        if sender is None: sender = addr
        if msg_id is not None:
            msg = Message(event, addr, insist, sender, msg_id)
        else:
            msg = Message(event, addr, insist, sender)
        self.broadcast(msg)

    @staticmethod
    def __insistence(lifetime):
        # TODO: find a better formula for this
        return 0.3 * lifetime

    @staticmethod
    def __valid_message(msg):
        return Message.get(msg.id) is None and not msg.has_expired()
