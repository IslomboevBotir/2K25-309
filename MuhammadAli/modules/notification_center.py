from smartcity.observer import Observer

class NotificationCenter(Observer):
    def update(self, msg): print(f"   Markaz: {msg}")

class MobileApp(Observer):
    def update(self, msg): print(f"   Telefon: {msg}")