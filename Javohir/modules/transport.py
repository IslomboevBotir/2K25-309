class TransportSystem:
    def __init__(self):
        self.buses = 50

    def show_routes(self):
        print("Transport marshrutlari ko‘rsatilmoqda: 1A, 2B, 77, 88")

    def add_bus(self):
        self.buses += 1
        print(f"Yangi avtobus qo‘shildi! Jami: {self.buses}")
