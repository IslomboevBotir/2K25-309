"""
Energy System with Builder Pattern

Design Pattern: BUILDER
Purpose: Construct complex energy sources step-by-step
"""

from abc import ABC, abstractmethod


class EnergySource(ABC):
    """Abstract energy source"""
    
    def __init__(self):
        self.location = ""
        self.capacity = 0
        self.current_output = 0
        self.efficiency = 0
        self.is_active = False
        self.components = []
    
    @abstractmethod
    def generate_energy(self):
        pass
    
    def get_status(self) -> str:
        status = "Active" if self.is_active else "Inactive"
        return f"{self.location}: {self.current_output}kW / {self.capacity}kW ({status})"


class SolarPanel(EnergySource):
    """Solar panel energy source"""
    
    def generate_energy(self):
        if self.is_active:
            self.current_output = int(self.capacity * self.efficiency)
            print(f"☀️ Solar panels at {self.location} generating {self.current_output}kW")
        else:
            print(f"☀️ Solar panels at {self.location} are inactive")


class WindTurbine(EnergySource):
    """Wind turbine energy source"""
    
    def generate_energy(self):
        if self.is_active:
            self.current_output = int(self.capacity * self.efficiency)
            print(f"💨 Wind turbines at {self.location} generating {self.current_output}kW")
        else:
            print(f"💨 Wind turbines at {self.location} are inactive")


class EnergySourceBuilder(ABC):
    """
    Builder Pattern Base Class
    Constructs energy sources step-by-step
    """
    
    def __init__(self):
        self._energy_source = None
    
    @abstractmethod
    def create_source(self):
        pass
    
    def set_location(self, location: str):
        self._energy_source.location = location
        return self
    
    def set_capacity(self, capacity: int):
        self._energy_source.capacity = capacity
        return self
    
    def set_efficiency(self, efficiency: float):
        self._energy_source.efficiency = efficiency
        return self
    
    def add_component(self, component: str):
        self._energy_source.components.append(component)
        return self
    
    def build(self) -> EnergySource:
        """Return the constructed energy source"""
        return self._energy_source


class SolarPanelBuilder(EnergySourceBuilder):
    """Builder: Constructs solar panel installations"""
    
    def create_source(self):
        self._energy_source = SolarPanel()
        return self
    
    def add_inverter(self):
        """Add solar-specific component"""
        self.add_component("DC-AC Inverter")
        return self
    
    def add_battery_storage(self):
        """Add battery storage"""
        self.add_component("Battery Storage")
        return self


class WindTurbineBuilder(EnergySourceBuilder):
    """Builder: Constructs wind turbine installations"""
    
    def create_source(self):
        self._energy_source = WindTurbine()
        return self
    
    def add_gearbox(self):
        """Add wind-specific component"""
        self.add_component("Gearbox")
        return self
    
    def add_rotor_blades(self, count: int):
        """Add rotor blades"""
        self.add_component(f"{count} Rotor Blades")
        return self


class EnergyDirector:
    """
    Director Pattern
    Orchestrates the building process
    """
    
    def __init__(self, builder: EnergySourceBuilder):
        self._builder = builder
    
    def construct_basic_solar(self, location: str) -> EnergySource:
        """Construct a basic solar installation"""
        return (self._builder
                .create_source()
                .set_location(location)
                .set_capacity(100)
                .set_efficiency(0.8)
                .add_component("Solar Panels")
                .build())
    
    def construct_advanced_solar(self, location: str) -> EnergySource:
        """Construct an advanced solar installation"""
        return (self._builder
                .create_source()
                .set_location(location)
                .set_capacity(500)
                .set_efficiency(0.9)
                .add_component("High-Efficiency Solar Panels")
                .add_inverter()
                .add_battery_storage()
                .build())
    
    def construct_basic_wind(self, location: str) -> EnergySource:
        """Construct a basic wind installation"""
        return (self._builder
                .create_source()
                .set_location(location)
                .set_capacity(200)
                .set_efficiency(0.7)
                .add_rotor_blades(3)
                .build())
    
    def construct_advanced_wind(self, location: str) -> EnergySource:
        """Construct an advanced wind installation"""
        return (self._builder
                .create_source()
                .set_location(location)
                .set_capacity(800)
                .set_efficiency(0.85)
                .add_rotor_blades(3)
                .add_gearbox()
                .add_component("Advanced Control System")
                .build())