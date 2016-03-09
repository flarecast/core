class Reactor():

    def __init__(self):
        self.events = {}

        for c in self.__class__.__subclasses__():
            plugin = c()
            events = c.events
            for e in events:
                events[e] = plugin 

    def react(self, warning):
        self[event.kind].react(warning)
