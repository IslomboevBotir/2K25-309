class Logger:
    __instance = None

    def __init__(self):
        if Logger.__instance:
            raise Exception("Logger — bu Singleton (bitta nusxa bo‘lishi kerak)")

    @staticmethod
    def get_instance():
        """
        Singleton — tizimda faqat bitta logger ishlaydi
        """
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def log(self, text):
        print(f"[LOG] {text}")
