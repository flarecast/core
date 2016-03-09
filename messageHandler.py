class MessageHandler():
    _singleton = None

    # Singleton Pattern implementation
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(MessageHandler, cls).__new__(cls)
        return cls._singleton

    def __init__(self, plugin):
        self.plugin = plugin