"""
Energy Manager - Uses Builder Pattern
"""

from modules.energy.energy_system import (
    SolarPanelBuilder, WindTurbineBuilder, EnergyDirector
)


class EnergyManager:
    """Manages all energy sources using builder pattern"""
    
    def __init__(self):
        self._energy_sources = {}
    
    def activate_source(self, location: str, source_type: str):
        """Activate energy source at location"""
        if location not in self._energy_sources:
            # Build energy source using builder pattern
            if source_type == "solar":
                builder = SolarPanelBuilder()
                director = EnergyDirector(builder)
                source = director.construct_advanced_solar(location)
            elif source_type == "wind":
                builder = WindTurbineBuilder()
                director = EnergyDirector(builder)
                source = director.construct_advanced_wind(location)
            else:
                print(f"❌ Unknown source type: {source_type}")
                return
            
            self._energy_sources[location] = source
            print(f"✓ Built {source_type} energy source at {location}")
            print(f"  Capacity: {source.capacity}kW")
            print(f"  Efficiency: {source.efficiency * 100}%")
            print(f"  Components: {', '.join(source.components)}")
        
        # Activate and generate
        source = self._energy_sources[location]
        source.is_active = True
        source.generate_energy()
    
    def get_status(self) -> str:
        """Get status of all energy sources"""
        if not self._energy_sources:
            return "  No energy sources installed"
        
        status = ""
        total_capacity = 0
        total_output = 0
        
        for location, source in self._energy_sources.items():
            status += f"  - {source.get_status()}\n"
            total_capacity += source.capacity
            total_output += source.current_output
        
        status += f"\n  Total: {total_output}kW / {total_capacity}kW\n"
        
        return status