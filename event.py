import time

class Event():
    def __init__(self, location, direction, kind, ownWarning,timestamp, lifetime):
        self.location
        self.direction
        self.kind
        self.ownWarning
        self.timestamp
        self.lifetime

    def has_expired(self):
        return (timestamp+lifetime) > time.time()
  