from logger import Logger

class SecurityProxy:
    def __init__(self, system, password="nigga"):
        self.system = system
        self.passwd = password
        self.log = Logger.get_instance()

    def monitor(self, pwd):
        if pwd == self.passwd:
            self.system.monitor()
        else:
            self.log.log("Kirish rad etildi (noto‘g‘ri parol)")
