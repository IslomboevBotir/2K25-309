class TrafficSchedule:
    def __init__(self):
        self.routes = []
        self.peak_hours = None
        self.light_timing = None

class TrafficBuilder:
    def __init__(self):
        self.schedule = TrafficSchedule()

    def add_route(self, route: str):
        self.schedule.routes.append(route)
        return self

    def set_peak_hours(self, hours: str):
        self.schedule.peak_hours = hours
        return self

    def set_light_timing(self, timing: int):
        self.schedule.light_timing = timing
        return self

    def build(self):
        print("\n📅 Traffic schedule built:")
        print(f"Routes: {self.schedule.routes}")
        print(f"Peak Hours: {self.schedule.peak_hours}")
        print(f"Light Timing: {self.schedule.light_timing}s")
        print("--------------------------------\n")
        return self.schedule
