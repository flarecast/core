class Message():
    currId = 0
    def __init__(self, event, addr, insistence, sender):
        self.event = event
        self.addr = addr
        self.insistence = insistence
        self.sender = sender
        self.id = currId
        currId = currId + 1

    def fullId(self):
        return self.id+"-"+self.sender

    def has_expired(self):
        return event.has_expired