class EventProcessor():
  def process (message):
    return {
    #example
        0: forward(message),
        1: forward(message)
            react(message)

    }.get(message.kind, "nothing")

def forward(self, message):
  #send to Connection Plugin to send to other users

def react(self, message):
  #send to the reactors