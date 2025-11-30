from factory import ModuleFactory

class SmartCityBuilder:
    """
    Builder — SmartCity tizimini qadam-qadam yig‘adi
    """
    def __init__(self):
        self.city = {}

    def add_lighting(self):
        self.city["lighting"] = ModuleFactory.create("lighting")
        return self

    def add_transport(self):
        self.city["transport"] = ModuleFactory.create("transport")
        return self

    def add_security(self):
        self.city["security"] = ModuleFactory.create("security")
        return self

    def add_energy(self):
        self.city["energy"] = ModuleFactory.create("energy")
        return self

    def build(self):
        return self.city
