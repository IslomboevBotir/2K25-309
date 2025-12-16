# 🧩 SmartCity System — Design Patterns Focus

Author: Jasur Shermatov

---

## Overview

SmartCity is a console application that simulates core subsystems of a modern city: lighting, transport, security, and energy. The architecture is intentionally crafted to demonstrate practical usage of classic object‑oriented design patterns. This README explains the patterns, why they were chosen, and where they are implemented in the codebase.

Project entry point: `main.py`  
Primary facade: `core/controller.py`

---

## How to Run

1. Ensure you have Python 3.10+ installed.
2. From the folder `Jasur Shermatov/`, run:

```
python3 main.py
```

Optional: quick test script

```
python3 test.py
```

---

## Architecture at a Glance

- `core/controller.py` — Central coordinator (Facade + Singleton)
- `core/adapter/weather_adapter.py` — Weather service integration (Adapter)
- `core/builder/traffic_builder.py` — Traffic plan assembly (Builder)
- `core/factory/factory.py` — Subsystem creation (Factory Method / Simple Factory)
- `modules/lighting/lighting_module.py` — Lighting hierarchy (Composite) and runtime augmentation (Decorator)
- `modules/transport/transport_module.py` — Transport subsystem
- `modules/security/security_module.py` — Security subsystem
- `modules/energy/energy_module.py` — Energy monitoring and optimization

---

## Design Patterns Used

### 1) Singleton + Facade — `core/controller.py`

- Intent:
  - Singleton: ensure a single, globally accessible instance of the system controller.
  - Facade: provide a simplified, unified interface to multiple complex subsystems.
- Where/How:
  - Singleton: `Controller.__new__` caches `_instance`; `__init__` guards with `_initialized` to avoid reinit.
  - Facade: public methods like `system_status()`, `toggle_city_lights()`, `start_traffic_system()`, `detect_threat()`, `monitor_energy()`, `simulate_weather()` orchestrate subsystems without exposing their internals to the UI.
- Code refs:
  - `Jasur Shermatov/core/controller.py`

Why it matters: The console UI (`main.py`) stays clean and focused on user flows, while `Controller` centralizes coordination. This improves maintainability and reduces coupling.

### 2) Adapter — `core/adapter/weather_adapter.py`

- Intent: Convert the interface of an external or legacy service to the interface expected by our app.
- Where/How:
  - `WeatherProvider.fetch()` returns a raw dict (external shape).
  - `WeatherAdapter.get_weather()` translates it into a domain object `WeatherInfo` with stable fields.
- Code refs:
  - `Jasur Shermatov/core/adapter/weather_adapter.py`

Why it matters: The app remains insulated from provider-specific response formats, enabling easy provider swaps or schema changes.

### 3) Builder — `core/builder/traffic_builder.py`

- Intent: Construct a complex object step by step, keeping construction separate from representation.
- Where/How:
  - `TrafficBuilder` fluently builds a `TrafficSchedule` by chaining `add_route()`, `set_peak_hours()`, `set_light_timing()`, then `build()`.
- Code refs:
  - `Jasur Shermatov/core/builder/traffic_builder.py`

Why it matters: Enhances readability and extensibility when creating rich schedules. New steps can be added without breaking callers.

### 4) Composite — `modules/lighting/lighting_module.py`

- Intent: Treat individual objects and compositions uniformly.
- Where/How:
  - `Light` defines a common interface.
  - `BasicLight` is a leaf; `LightGroup` is a composite that holds `Light` children and forwards `turn_on/turn_off/status` to them.
  - `LightingModule` builds a city-wide tree of lights via a root `LightGroup`.
- Code refs:
  - `Jasur Shermatov/modules/lighting/lighting_module.py`

Why it matters: Enables hierarchical control (turn on/off a single light or an entire group) with the same operations.

### 5) Decorator — `modules/lighting/lighting_module.py`

- Intent: Add behavior to objects dynamically without changing their classes.
- Where/How:
  - `LoggingDecorator` wraps any `Light` and adds logging to `turn_on/turn_off` while delegating to the wrapped instance.
  - `LightingModule` composes `LoggingDecorator(BasicLight(i))` to enrich lights with logs at runtime.
- Code refs:
  - `Jasur Shermatov/modules/lighting/lighting_module.py`

Why it matters: Cross-cutting concerns (like logging) are added non-invasively, avoiding subclass explosion.

### 6) Factory Method (Simple Factory) — `core/factory/factory.py`

- Intent: Encapsulate object creation logic and centralize instance selection.
- Where/How:
  - `ModuleFactory.create_module(name)` returns instances of subsystem modules based on a string key.
  - While implemented as a Simple Factory (static selector), it illustrates the Factory Method intent of delegating creation logic.
- Code refs:
  - `Jasur Shermatov/core/factory/factory.py`

Why it matters: New modules can be integrated by extending the factory’s selection logic, keeping creation concerns in one place.

---

## Key Flows

- Start application: `main.py` presents a console menu and calls into `Controller` (Facade).
- Lighting control: `Controller.toggle_city_lights()` delegates to `LightingModule.root_group` (Composite + Decorator).
- Traffic system: invoked via `Controller.start_traffic_system()`; traffic planning uses `TrafficBuilder`.
- Weather simulation: `Controller.simulate_weather()` uses `WeatherAdapter` to normalize provider data.
- Security and Energy: accessed through `Controller` methods; encapsulated per module.

---

## Extensibility Notes

- Add a new module: implement a subsystem under `modules/`, expose a cohesive API, and register it in `ModuleFactory` and/or wire it in `Controller`.
- Replace weather provider: create a new provider with `fetch()` and plug it into `WeatherAdapter` or a new adapter variant.
- Evolve lighting: add new `Light` implementations; they will work seamlessly with `LightGroup` and optional `LoggingDecorator`.
- Expand schedules: extend `TrafficBuilder` with more steps (e.g., lane priorities) without breaking clients.

---

## Author

Prepared by: Jasur Shermatov  
Role: Developer (Architecture & Implementation)  
Focus: Demonstration of classic design patterns in a cohesive SmartCity simulation.
