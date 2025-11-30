class Logger:
    _instance = None

    def __init__(self):
        if Logger._instance is not None:
            raise Exception('Logger is a singleton!')
        self.logs = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Logger()
        return cls._instance

    def log(self, message):
        self.logs.append(message)
        print(f'[LOG] {message}')
