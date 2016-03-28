import threading
from detector import *
from event import *

class TestDetector(Detector):

    @on_event
    def wait_input(self):
        text = input("> ")
        print("RECEIVED INPUT")
        return Event(1, 1, "input", False, time.time(), 10000, text )

    def run(self):
        self.wait_input()
