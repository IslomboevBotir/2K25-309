from core.builders.report_builder import ReportBuilder

class EnergySubsystem:
    def __init__(self):
        self.usage_kw = [12.5, 11.7, 13.0]

    def generate_report(self):
        b = ReportBuilder()
        b.add_header('Energy Report')
        b.add_section('Usage (kW)', str(self.usage_kw))
        avg = sum(self.usage_kw)/len(self.usage_kw)
        b.add_section('Average (kW)', f'{avg:.2f}')
        b.add_footer('End of Energy Report')
        print(b.build())
