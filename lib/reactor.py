class Reactor():
    event_kinds = {}

    @classmethod
    def add_plugin_events(cls):
        for c in cls.__subclasses__():
            plugin = c()
            ek = c.event_kinds
            for e in ek:
                if e in cls.event_kinds.keys():
                    cls.event_kinds[e].append(plugin)
                else:
                    cls.event_kinds[e] = [plugin]

    @classmethod
    def react(cls, alert):
        if not alert.kind in cls.event_kinds.keys():
            return None

        for reactor in cls.event_kinds[alert.kind]:
            reactor.react(alert)
