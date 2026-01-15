class TrafficSchedule:
    def __init__(self, routes, peak_hours, light_timing):
        self.routes = routes
        self.peak_hours = peak_hours
        self.light_timing = light_timing


class TrafficBuilder:
    def __init__(self):
        self._routes = []
        self._peak_hours = None
        self._light_timing = None

    def add_route(self, route: str):
        self._routes.append(route)
        return self

    def set_peak_hours(self, hours: str):
        self._peak_hours = hours
        return self

    def set_light_timing(self, timing: int):
        self._light_timing = timing
        return self

    def build(self):
        if not self._routes:
            raise ValueError("At least one route is required")
        if self._light_timing is None:
            raise ValueError("Light timing must be set")

        return TrafficSchedule(
            routes=self._routes,
            peak_hours=self._peak_hours,
            light_timing=self._light_timing
        )
