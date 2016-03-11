from circuits import Component, Event, handler
from message_handler import MessageHandler

class msg_received(Event):
    """Message Received Event"""

class event_received(Event):
    """Event Received Event"""

class EventProcessor(Component):
    MSG_RECEIVED = 1
    EVENT_RECEIVED = 2

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(EventProcessor, cls).__new__(cls)
        return cls._singleton

    def __init__(self):
        super(EventProcessor, self).__init__()
        self.messenger = MessageHandler(self)

    @handler("msg_received")
    def msg_received(self, *args):
        self.react_external(args[0])

    @handler("event_received")
    def event_received(self, event):
        self.rect_internal(event)

    def react_external(self, event):
        print("RECEIVED EXTERNAL EVENT: " + event)

    def react_internal(self, event):
        print("RECEIVED INTERNAL EVENT")

