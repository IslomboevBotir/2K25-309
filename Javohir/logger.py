class Logger:
    _instance = None

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("Bu klass Singleton!")
        self.logs = []

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG] {message}")
