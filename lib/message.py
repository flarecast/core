class Message():
    current_id = 0
    def __init__(self, event, addr, insistence, sender):
        self.event = event
        self.addr = addr
        self.insistence = insistence
        self.sender = sender
        self.id = Message.current_id
        Message.current_id += 1

    def full_id(self):
        return self.id+"-"+self.sender

    def has_expired(self):
        return event.has_expired
