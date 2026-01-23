"""
Transport Management Subsystem
"""

class TransportSystem:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def get_status(self):
        if not self.vehicles:
            return "🚦 Transport System: No vehicles registered"
        
        status = "🚦 Transport System Status:\n"
        for vehicle in self.vehicles:
            status += f"   - {vehicle.get_status()}\n"
        return status
    
    def operate_all(self):
        results = []
        for vehicle in self.vehicles:
            results.append(vehicle.move())
        return results