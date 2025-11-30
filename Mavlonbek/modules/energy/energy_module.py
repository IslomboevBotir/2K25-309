# FIO/modules/energy/energy_module.py

from FIO.core.proxy.proxy import EnergyDataProxy

class EnergyModule:
    """
    Integrates the Proxy pattern for controlled access to energy data.
    """
    def __init__(self):
        # The module interacts with the Proxy, not the Real Subject directly
        self._data_proxy = EnergyDataProxy()
        print("Energy Module: Initialized with EnergyDataProxy for access control.")

    def start_monitoring(self):
        print("Energy Module: Energy monitoring started.")
        print(self._data_proxy.get_basic_data())

    def report_usage(self):
        print("Energy Module: Generating basic usage report.")
        print(self._data_proxy.get_basic_data())

    def get_sensitive_data(self, user_role):
        """Accesses sensitive data via the Proxy."""
        print(self._data_proxy.get_sensitive_data(user_role))

    def get_status(self):
        print("Energy Module Status: Monitoring active. Basic data available.")
