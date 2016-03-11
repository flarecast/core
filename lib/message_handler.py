from connection_plugin import ConnectionPlugin
import threading

def on_message(f):
    def callback(*args):
        event = f(*args)
        MessageHandler._singleton.handle(event)

    return callback

class MessageHandler():
    _singleton = None

    # Singleton Pattern implementation
    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super(MessageHandler, cls).__new__(cls)
        return cls._singleton

    def __init__(self, processor=None):
        self.processor = processor
        self.plugin = ConnectionPlugin.active_plugin()
        self.plugin.start()

    def broadcast(self, msg):
        if( self.__process_message(msg) ):
            self.plugin.broadcast(msg)
            self.__clear_messages()

    def emit_event(self, event):
        addr = plugin.address()
        insist = __insistance(event.lifetime)
        msg = Message(event, addr, insist, sender)
        self.broadcast(msg)

    def handle(self, event):
        from event_processor import msg_received
        self.processor.fire(msg_received(event))

    def __insistance(lifetime):
        # TODO: find a better formula for this
        return 0.3 * lifetime

    def __was_processed(msgs, msg):
        for m in msgs:
            if m.full_id() == msg.full_id():
                return False

        return True

    def __process_message(self, msg):
        b = not __was_processed(self.processed_messages, msg)
        if b: self.processed_messages.append(msg)
        return b

    def __clear_messages(self):
        self.processed_messages = [m for m in self.processed_messages if not m.has_expired()] # ily Python
