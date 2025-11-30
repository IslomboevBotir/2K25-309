# FIO/core/proxy/proxy.py

# --- Subject Interface ---

class EnergyDataService:
    """The interface for accessing energy data."""
    def get_basic_data(self):
        raise NotImplementedError

    def get_sensitive_data(self):
        raise NotImplementedError

# --- Real Subject ---

class RealEnergyDataService(EnergyDataService):
    """The actual service that performs the sensitive operation."""
    def get_basic_data(self):
        return "Basic Energy Data: Current city-wide consumption is 1500 MWh."

    def get_sensitive_data(self):
        # Simulate a time-consuming or resource-intensive operation
        return "Sensitive Energy Data: Detailed breakdown of consumption by critical infrastructure (Power Plant 1: 400 MWh, Data Center: 200 MWh)."

# --- Proxy ---

class EnergyDataProxy(EnergyDataService):
    """
    Design Pattern: Proxy (Structural)
    Purpose: Provides a surrogate or placeholder for another object (RealEnergyDataService)
             to control access to it.
    Usage: Implements access control (protection proxy) for sensitive energy data.
    """
    def __init__(self):
        self._real_service = None
        self._allowed_roles = ["Admin", "Energy Manager"]

    def _check_access(self, user_role):
        """Pre-check for access control."""
        print(f"Proxy: Checking access for role '{user_role}'...")
        if user_role in self._allowed_roles:
            print("Proxy: Access granted.")
            return True
        print("Proxy: Access denied. Insufficient privileges.")
        return False

    def _get_real_service(self):
        """Lazy initialization of the Real Subject."""
        if self._real_service is None:
            print("Proxy: Initializing RealEnergyDataService...")
            self._real_service = RealEnergyDataService()
        return self._real_service

    def get_basic_data(self):
        # Basic data is always accessible
        return self._get_real_service().get_basic_data()

    def get_sensitive_data(self, user_role):
        if self._check_access(user_role):
            return self._get_real_service().get_sensitive_data()
        else:
            return "Access Denied: Cannot retrieve sensitive energy data."
