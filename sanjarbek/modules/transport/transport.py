# modules/transport/transport.py

class TransportSystem:
    """
    Transport subsystem (domain module).
    Purpose: Manage public transport dispatching and keep simple operational state.

    This file is intentionally pattern-free: it represents core business logic.
    Patterns will be applied in core layer (Factory, Facade, etc.).
    """

    def __init__(self, max_buses: int = 10):
        self.max_buses = max_buses
        self.active_routes: list[str] = []

    def dispatch(self, route: str) -> str:
        """
        Dispatch a bus to a given route if capacity allows.
        """
        route = route.strip()
        if not route:
            return "Transport: route name cannot be empty."

        if len(self.active_routes) >= self.max_buses:
            return f"Transport: cannot dispatch, max buses reached ({self.max_buses})."

        self.active_routes.append(route)
        return f"Transport: bus dispatched to route {route}."

    def status(self) -> str:
        """
        Return a human-readable status for console/report.
        """
        return (
            f"Transport: max_buses={self.max_buses}, "
            f"active_routes={self.active_routes}"
        )
