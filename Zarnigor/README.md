# SmartCity System

SmartCity System is a console-based simulation of an intelligent city management platform.  
The application demonstrates how different urban subsystems—transportation, lighting, security, and energy—can be coordinated through a unified controller using object‑oriented programming and classic design patterns.

The project is structured to be modular, extensible, and easy to maintain.  
At least five design patterns are implemented, each serving a functional purpose in the system.

---

## ✅ Features

- Centralized SmartCity controller (Facade + Singleton)
- Modular subsystems:
  - Transport management
  - Lighting control
  - Security monitoring
  - Energy consumption tracking
- Console-based user interaction
- Integration with an external weather service (via Adapter)
- Access control for restricted subsystems (via Proxy)
- Report generation using Builder pattern
- Abstract Factory for subsystem creation

---

## ✅ Implemented Design Patterns

### 1. **Singleton**
Used in:
- `controller.py` — ensures only one SmartCity controller exists.
- `logger.py` — global logging instance.

### 2. **Facade**
- `controller.py` acts as a unified interface to all subsystems.

### 3. **Abstract Factory + Factory Method**
- `factory.py` creates subsystem objects (transport, lighting, security, energy).

### 4. **Builder**
- `builder.py` constructs multi-step city reports.

### 5. **Adapter**
- `adapter.py` adapts an external weather API to the system interface.

### 6. **Proxy**
- `proxy.py` controls access to sensitive subsystems (e.g., security).

---

## ✅ Project Structure

The project follows a minimalistic structure:  
**each folder contains only `__init__.py` and one `.py` file**, as required.

