from core.factories.device_factory import DeviceFactory, EnergySavingFactory

class Light:
    def __init__(self, device):
        self.device = device
        self.on = False

    def turn_on(self):
        self.on = True
        print(f'{self.device.info()} -> ON')

    def turn_off(self):
        self.on = False
        print(f'{self.device.info()} -> OFF')

    def status(self):
        return f'{self.device.info()} (on={self.on})'

class EnergySavingDecorator(Light):
    def __init__(self, light):
        self._wrapped = light

    def turn_on(self):
        print('(EnergySavingDecorator) reducing brightness...')
        self._wrapped.turn_on()

    def turn_off(self):
        self._wrapped.turn_off()

    def status(self):
        return '(Eco) ' + self._wrapped.status()

class Zone:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, light):
        self.children.append(light)

    def turn_all_on(self):
        print(f'Zone {self.name}: turning all on')
        for l in self.children:
            l.turn_on()

    def turn_all_off(self):
        print(f'Zone {self.name}: turning all off')
        for l in self.children:
            l.turn_off()

    def status(self):
        return [c.status() for c in self.children]

class LightingSubsystem:
    def __init__(self, factory: DeviceFactory):
        self.factory = factory
        self.zone = Zone('Central')
        for _ in range(3):
            dev = factory.create_light()
            light = Light(dev)
            if isinstance(factory, EnergySavingFactory):
                light = EnergySavingDecorator(light)
            self.zone.add(light)

    def turn_all_on(self):
        self.zone.turn_all_on()

    def turn_all_off(self):
        self.zone.turn_all_off()

    def status(self):
        print('\n'.join(self.zone.status()))
