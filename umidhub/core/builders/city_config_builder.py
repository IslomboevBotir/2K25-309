"""
Builder Pattern - constructs complex objects step by step
Used for: Building city configuration with multiple subsystems
"""

class CityConfig:
    def __init__(self):
        self.transport_enabled = False
        self.lighting_enabled = False
        self.security_enabled = False
        self.energy_monitoring = False
        self.sensor_integration = False
        self.city_name = "SmartCity"
    
    def __str__(self):
        return f"""
╔══════════════════════════════════════╗
║   {self.city_name} Configuration     
╚══════════════════════════════════════╝
🚦 Transport System:    {'✅ Enabled' if self.transport_enabled else '❌ Disabled'}
💡 Lighting System:     {'✅ Enabled' if self.lighting_enabled else '❌ Disabled'}
🔒 Security System:     {'✅ Enabled' if self.security_enabled else '❌ Disabled'}
⚡ Energy Monitoring:   {'✅ Enabled' if self.energy_monitoring else '❌ Disabled'}
📡 Sensor Integration:  {'✅ Enabled' if self.sensor_integration else '❌ Disabled'}
        """


class CityConfigBuilder:
    def __init__(self):
        self.config = CityConfig()
    
    def set_city_name(self, name):
        self.config.city_name = name
        return self
    
    def enable_transport(self):
        self.config.transport_enabled = True
        return self
    
    def enable_lighting(self):
        self.config.lighting_enabled = True
        return self
    
    def enable_security(self):
        self.config.security_enabled = True
        return self
    
    def enable_energy_monitoring(self):
        self.config.energy_monitoring = True
        return self
    
    def enable_sensors(self):
        self.config.sensor_integration = True
        return self
    
    def build(self):
        return self.config