from reactor import Reactor

class TestReactor(Reactor):
    event_kinds = {"input"}

    def react(self, alert):
        print("RECEIVED INPUT: " + alert.extra)
        print("IT WAS ", alert.distance, "m FROM HERE")
