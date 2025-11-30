class SecuritySystem:
    def __init__(self):
        self.armed = False

    def status(self):
        return f'Security armed={self.armed}'

    def arm(self):
        self.armed = True
