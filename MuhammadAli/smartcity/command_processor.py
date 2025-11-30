class CommandProcessor:
    @staticmethod
    def process(cmd: str, ctrl):
        parts = cmd.lower().split()
        if not parts:
            return True

        match parts:
            case ["transport" | "1"]:
                ctrl.manage_transport()
            case ["lighting" | "light" | "2"]:
                ctrl.manage_lighting()
            case ["camera", pwd]:
                ctrl.access_security_camera(pwd)
            case ["energy" | "4"]:
                ctrl.monitor_energy()
            case ["weather" | "5"]:
                ctrl.get_weather()
            case ["waste" | "6"]:
                ctrl.manage_waste()
            case ["wifi" | "7"]:
                ctrl.manage_wifi()
            case ["traffic", *modes]:
                ctrl.change_traffic_mode(" ".join(modes))
            case ["report" | "r"]:
                ctrl.full_report()
            case ["help" | "h" | "?"]:
                print("\nYORDAM:\ntransport, lighting, camera, energy, weather, waste, wifi, traffic rush, report, help, exit")
            case ["exit" | "0"]:
                return False
            case _:
                print("Noma'lum buyruq! 'help' yozing")
        return True
