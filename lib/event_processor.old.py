class EventProcessor():

    def __init__(self, messageHandler, reactor):
        self.messageHandler = messageHandler
        self.reactor = reactor

    def process(self, event):
        forward(event)
        if event.ownWarning:
            react_internal(event)

    def react_external(self, event):
        distance = compute_distance(event.location)
        warning = Warning(event, distance)
        reactor.react(warning)

    def react_internal(self, event):
        warning = Warning(event)
        reactor.react(warning)

    def forward(self, event):
        messageHandle.handle(event)

    def compute_distance(location):
        #currlocation - location