"""
Transportation Manager - Factory Method Implementation
"""

from core.factories.device_factory import DeviceFactory, SmartDevice
from modules.transport.transport_system import TrafficLight, PublicTransport


class TrafficLightFactory(DeviceFactory):
    """Factory Method: Creates traffic lights"""
    
    def create_device(self, device_id: str, location: str) -> SmartDevice:
        return TrafficLight(device_id, location)


class PublicTransportFactory(DeviceFactory):
    """Factory Method: Creates public transport"""
    
    def create_device(self, device_id: str, location: str) -> SmartDevice:
        return PublicTransport(device_id, location)


class TransportManager:
    """Manages all transportation devices"""
    
    def __init__(self):
        self._traffic_lights = {}
        self._public_transports = {}
        self._traffic_factory = TrafficLightFactory()
        self._transport_factory = PublicTransportFactory()
        self._device_counter = 0
    
    def control_traffic_light(self, location: str, state: str):
        """Control traffic light at location"""
        if location not in self._traffic_lights:
            self._device_counter += 1
            device_id = f"TL{self._device_counter:03d}"
            light = self._traffic_factory.deploy_device(device_id, location)
            light.activate()
            self._traffic_lights[location] = light
        
        self._traffic_lights[location].set_state(state)
    
    def control_public_transport(self, route: str, action: str):
        """Control public transport"""
        if route not in self._public_transports:
            self._device_counter += 1
            device_id = f"PT{self._device_counter:03d}"
            transport = self._transport_factory.deploy_device(device_id, route)
            self._public_transports[route] = transport
        
        transport = self._public_transports[route]
        if action == "start":
            transport.activate()
        elif action == "stop":
            transport.deactivate()
    
    def get_status(self) -> str:
        """Get status of all transport devices"""
        status = ""
        if self._traffic_lights:
            status += "  Traffic Lights:\n"
            for light in self._traffic_lights.values():
                status += f"    - {light.get_status()}\n"
        
        if self._public_transports:
            status += "  Public Transport:\n"
            for transport in self._public_transports.values():
                status += f"    - {transport.get_status()}\n"
        
        return status if status else "  No active devices"