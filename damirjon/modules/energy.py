# energy.py
# PATTERN: Builder – energiya monitoring obyektini bosqichma-bosqich qurish.

class EnergyReport:
    """Final product created by Builder"""
    def __init__(self):
        self.data = {}

    def show(self):
        print("[Energy Report]", self.data)

class EnergyReportBuilder:
    """Builder pattern"""

    def __init__(self):
        self.report = EnergyReport()

    def add_usage(self):
        self.report.data["usage"] = "250 kWh"
        return self

    def add_efficiency(self):
        self.report.data["efficiency"] = "92%"
        return self

    def add_warnings(self):
        self.report.data["warnings"] = "None"
        return self

    def build(self):
        return self.report

class EnergySystem:
    """Energy subsystem using Builder pattern"""

    def optimize_energy(self):
        print("[Energy] Optimizing energy system...")

        builder = EnergyReportBuilder()
        report = (
            builder
            .add_usage()
            .add_efficiency()
            .add_warnings()
            .build()
        )

        report.show()
