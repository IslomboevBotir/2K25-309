# SmartCity System

## Project Description
The SmartCity System is a console application that simulates the operation of an intelligent city management system. It combines various subsystems responsible for lighting, transportation, security, and energy management. The system is implemented in Python using Object-Oriented Programming principles and incorporates several design patterns to ensure architectural stability and extensibility.

## Design Patterns Used
The following design patterns are implemented in the system:

1.  **Singleton:** Ensures a single instance of the `SmartCityController`.
2.  **Facade:** Provides a simplified interface to the complex subsystem operations via the `SmartCityController`.
3.  **Abstract Factory:** Used to create families of related objects (e.g., different types of sensors and actuators) without specifying their concrete classes.
4.  **Factory Method:** Used within the `TransportModule` to create different types of vehicles (e.g., Bus, Tram) based on user input.
5.  **Adapter:** Used to integrate an external, legacy `SecurityCamera` into the modern `SecurityModule`.
6.  **Proxy:** Used to control access to the sensitive `EnergyModule` operations.

## Project Structure

```
FIO/
├── main.py             # Main application entry point
├── test.py             # Test suite for system components
├── core/
│   ├── controller.py   # Central controller (Singleton, Facade)
│   ├── factories/      # Abstract Factory implementation
│   ├── adapters/       # Adapter implementation
│   ├── proxy/          # Proxy implementation
│   └── singleton/      # Singleton base class
├── modules/            # Smart city subsystems
│   ├── transport/      # Transportation management (Factory Method)
│   ├── lighting/       # Lighting management
│   ├── security/       # Security subsystem (Adapter)
│   └── energy/         # Energy saving and monitoring (Proxy)
└── README.md           # This file
```

## How to Run
1. Navigate to the `FIO/` directory.
2. Run the main application: `python3 main.py`

## How to Test
1. Navigate to the `FIO/` directory.
2. Run the test suite: `python3 test.py`
