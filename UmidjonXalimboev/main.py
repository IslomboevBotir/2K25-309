from core.controller import SmartCityController

def main():
    controller = SmartCityController.get_instance()
    controller.bootstrap()
    print("Welcome to SmartCity System (console). Type 'help' for commands.")
    while True:
        cmd = input('> ').strip().lower()
        if cmd in ('quit', 'exit'):
            print('Shutting down...')
            break
        elif cmd == 'help':
            print('commands: status, lights on, lights off, transport report, security status, energy report, weather, quit')
        elif cmd == 'status':
            controller.status()
        elif cmd == 'lights on':
            controller.lighting.turn_all_on()
        elif cmd == 'lights off':
            controller.lighting.turn_all_off()
        elif cmd == 'transport report':
            controller.transport.generate_report()
        elif cmd == 'security status':
            controller.security_proxy.get_status()
        elif cmd == 'energy report':
            controller.energy.generate_report()
        elif cmd == 'weather':
            controller.fetch_weather()
        else:
            print('Unknown command; try help')

if __name__ == '__main__':
    main()
