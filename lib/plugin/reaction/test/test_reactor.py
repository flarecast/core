from reactor import Reactor

class TestReactor(Reactor):
    event_kinds = {"input"}

    def react(self, alert):
        print("There was input, THIS INPUT: " + alert.extra)