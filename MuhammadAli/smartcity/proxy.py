class SecurityProxy:
    def __init__(self, real_system):
        self.real_system = real_system

    def access_cameras(self, password: str):
        if password == "smart2025":
            print("Parol to'g'ri — barcha kameralar ochildi!")
            self.real_system._stream_all()
            return True
        else:
            print("PAROL XATO! Kirish rad etildi")
            return False
