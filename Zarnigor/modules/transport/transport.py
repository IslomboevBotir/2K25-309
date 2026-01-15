"""
Transport subsystem of SmartCity.

Represents a simple model of public transport with buses and trams.
Can be extended in future to support routes, schedules, or more vehicle types.
"""


class TransportSystem:
    def __init__(self):
        # In a real system these might be dynamic, loaded from DB, etc.
        self.buses_running = 12
        self.trams_running = 3
        self.incidents_today = 0
        self.running = False

    def start_system(self) -> str:
        """
        Simulates starting the transport system.
        """
        self.running = True
        return "🚦 Transport system started: buses and trams are now running."

    def get_status(self) -> str:
        """
        Returns a human-readable text description of the transport state.
        """
        base = (
            f"Transport: {self.buses_running} buses and "
            f"{self.trams_running} trams in operation."
        )
        if self.incidents_today == 0:
            base += " No incidents reported today."
        else:
            base += f" Incidents today: {self.incidents_today}."
        if self.running:
            base += " System status: RUNNING."
        else:
            base += " System status: STOPPED."
        return base
