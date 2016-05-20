class Message():
    current_id = 0
    def __init__(self, event, addr, insistence, sender, msg_id = current_id):
        self.event = event
        self.addr = addr
        self.insistence = insistence
        self.sender = sender
        self.id = msg_id
        if(self.id == Message.current_id):
            Message.current_id += 1

    def full_id(self):
        return str(self.id)+'-'+str(self.sender)

    def has_expired(self):
        return self.event.has_expired
