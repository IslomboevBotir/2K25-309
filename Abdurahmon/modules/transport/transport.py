from core.factories.device_factory import DeviceFactory, EnergySavingFactory
from core.builders.report_builder import ReportBuilder

class TransportSubsystem:
    def __init__(self, factory: DeviceFactory):
        self.factory = factory
        self.fleet = [factory.create_transport_unit() for _ in range(2)]

    def generate_report(self):
        b = ReportBuilder()
        b.add_header('Transport Report')
        for idx, v in enumerate(self.fleet, 1):
            b.add_section(f'Unit {idx}', v.info())
        b.add_footer('End of report')
        print(b.build())
