import time

class Event():
    def __init__(self, location, direction, kind, ownWarning,timestamp, lifetime, extra = None):
        self.location = location 
        self.direction = direction
        self.kind = kind
        self.ownWarning = ownWarning
        self.timestamp = timestamp
        self.lifetime = lifetime
        self.extra = extra

    def has_expired(self):
        return (timestamp+lifetime) > time.time()
  