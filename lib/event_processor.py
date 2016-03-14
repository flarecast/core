from circuits import Component, Event, handler
from message_handler import MessageHandler
from reactor import Reactor
from detector import Detector
from alert import Alert

from reactor import Reactor
from detector import Detector
from alert import Alert

class msg_received(Event):
    """Message Received Event"""

class detection_received(Event):
    """Detection Received Event"""

class EventProcessor(Component):
    MSG_RECEIVED = 1
    DETECTION_RECEIVED = 2
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(EventProcessor, cls).__new__(cls)
        return cls._singleton

    def __init__(self):
        super(EventProcessor, self).__init__()
        #self.messageHandler = MessageHandler(self)
        Detector.start_plugins()
        Reactor.add_plugin_events()

    def react_external(self, event):
        distance = compute_distance(event.location)
        alert = Alert(event, distance)
        Reactor.react(alert)

    def react_internal(self, event):
        alert = Alert(event)
        Reactor.react(alert)

    def compute_distance(location):

        #TODO: currlocation - location
        return 13

    @handler("msg_received")
    def msg_received(self, *args):
        self.react_external(args[0])

    @handler("detection_received")
    def detection_received(self, *args):
        self.react_internal(args[0])
        #self.message_handler.emit_event(args[0])

    @classmethod
    def handle_detection(cls, event):
        cls._singleton.fire(detection_received(event))
    @classmethod
    def handle_message(cls, event):
        cls._singleton.fire(msg_received(event))

