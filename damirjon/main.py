# main.py
# This file runs the whole SmartCity system (Facade via Controller)

from core.controller import SmartCityController

def main():
    controller = SmartCityController()   # Facade + Singleton inside controller
    controller.start_system()

if __name__ == "__main__":
    main()
