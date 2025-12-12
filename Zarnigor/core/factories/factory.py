"""
Factory module.

Implements:
- Abstract Factory: SubsystemFactory creates families of related objects
  (transport, lighting, security, energy subsystems).
- Factory Method: each create_* method encapsulates object construction
  and can easily be extended or replaced with other implementations.
"""

from modules.transport.transport import TransportSystem
from modules.lighting.lighting import LightingSystem
from modules.security.security import SecuritySystem
from modules.energy.energy import EnergySystem


class SubsystemFactory:
    """
    Abstract Factory for subsystem creation.
    """

    def create_transport_system(self) -> TransportSystem:
        """
        Factory Method for TransportSystem.
        Could be extended to choose different transport types in future.
        """
        return TransportSystem()

    def create_lighting_system(self) -> LightingSystem:
        """
        Factory Method for LightingSystem.
        Currently uses Composite + Decorator internally.
        """
        return LightingSystem()

    def create_security_system(self) -> SecuritySystem:
        """
        Factory Method for SecuritySystem.
        """
        return SecuritySystem()

    def create_energy_system(self) -> EnergySystem:
        """
        Factory Method for EnergySystem.
        """
        return EnergySystem()
