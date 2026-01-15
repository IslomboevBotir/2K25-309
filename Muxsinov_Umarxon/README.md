🧩 SmartCity System — Design Patterns–Oriented Architecture

Author: Umarxon Muxsinov

Project Overview

SmartCity — bu konsol asosidagi simulyatsion dastur bo‘lib, zamonaviy shahar infratuzilmasining asosiy subsistemalarini modellashtiradi: yoritish, transport, xavfsizlik va energiya boshqaruvi. Loyiha arxitekturasi klassik Object-Oriented Design Patterns’ni amaliy misollar orqali ko‘rsatish maqsadida ongli ravishda ishlab chiqilgan.

Mazkur hujjat quyidagilarni tushuntiradi:

qaysi design pattern qayerda qo‘llangan,

nima sababdan tanlangan,

va ular tizimning umumiy arxitekturasiga qanday hissa qo‘shgan.

Entry point: main.py
Primary Facade: core/controller.py

How to Run the Application

Python 3.10 yoki undan yuqori versiyasi o‘rnatilgan bo‘lishi kerak.

Loyiha ildiz papkasidan quyidagi buyruqni ishga tushiring:

python3 main.py


Ixtiyoriy test skripti:

python3 test.py

High-Level Architecture

Quyida loyihaning asosiy komponentlari va ularning vazifalari keltirilgan:

core/controller.py — Markaziy boshqaruv (Singleton + Facade)

core/adapter/weather_adapter.py — Ob-havo servisiga moslashuv (Adapter)

core/builder/traffic_builder.py — Transport jadvalini bosqichma-bosqich yig‘ish (Builder)

core/factory/factory.py — Subsystem obyektlarini yaratish (Simple Factory / Factory Method)

modules/lighting/lighting_module.py — Yoritish ierarxiyasi (Composite) va dinamik xatti-harakat qo‘shish (Decorator)

modules/transport/transport_module.py — Transport boshqaruvi

modules/security/security_module.py — Xavfsizlik monitoringi

modules/energy/energy_module.py — Energiya nazorati va optimizatsiyasi

Design Patterns Breakdown
1. Singleton + Facade — core/controller.py

Intent:

Singleton: butun tizim bo‘ylab yagona boshqaruv obyektini ta’minlash.

Facade: murakkab subsistemalar ustidan soddalashtirilgan yagona interfeys taqdim etish.

Implementation:

Singleton __new__ orqali _instance ni kesh qiladi.

__init__ ichida _initialized flag yordamida qayta initsializatsiya oldi olinadi.

Facade sifatida Controller quyidagi metodlarni taqdim etadi:

system_status()

toggle_city_lights()

start_traffic_system()

detect_threat()

monitor_energy()

simulate_weather()

Code reference:
Umarxon Muxsinov/core/controller.py

Why it matters:
UI (konsol menyu) subsistemalarning ichki tuzilishini bilmaydi. Barcha muvofiqlashtirish bitta markazda jamlangan, bu esa coupling’ni kamaytiradi va kodni qo‘llab-quvvatlashni osonlashtiradi.

2. Adapter — core/adapter/weather_adapter.py

Intent:
Tashqi yoki legacy servis interfeysini tizim ichki modeliga moslashtirish.

Implementation:

WeatherProvider.fetch() — tashqi manbadan xom ma’lumot (dict) qaytaradi.

WeatherAdapter.get_weather() — ushbu ma’lumotni domen obyektiga (WeatherInfo) aylantiradi.

Code reference:
Umarxon Muxsinov/core/adapter/weather_adapter.py

Why it matters:
Agar ob-havo provider o‘zgarsa yoki response format yangilansa, tizimning qolgan qismi o‘zgarmaydi.

3. Builder — core/builder/traffic_builder.py

Intent:
Murakkab obyektni (TrafficSchedule) bosqichma-bosqich va o‘qilishi oson tarzda qurish.

Implementation:

Fluent interface:

add_route()

set_peak_hours()

set_light_timing()

build()

Code reference:
Umarxon Muxsinov/core/builder/traffic_builder.py

Why it matters:
Transport jadvali kengaytirilsa ham (masalan, lane priority), mavjud kod buzilmaydi.

4. Composite — modules/lighting/lighting_module.py

Intent:
Yakka obyektlar va ularning kompozitsiyalarini bir xil interfeys orqali boshqarish.

Implementation:

Light — umumiy interfeys

BasicLight — leaf

LightGroup — composite (ichida boshqa Light obyektlarini saqlaydi)

LightingModule — butun shahar bo‘yicha daraxt tuzilmasini yaratadi

Code reference:
Umarxon Muxsinov/modules/lighting/lighting_module.py

Why it matters:
Bitta chiroqni yoki butun hududni bir xil buyruqlar bilan boshqarish mumkin.

5. Decorator — modules/lighting/lighting_module.py

Intent:
Obyektga qo‘shimcha xatti-harakatni dinamik tarzda qo‘shish.

Implementation:

LoggingDecorator har qanday Light obyektini o‘rab, turn_on/turn_off jarayonlariga log qo‘shadi.

Asosiy obyekt sinfi o‘zgarmaydi.

Why it matters:
Logging kabi cross-cutting concern’lar subclass’lar sonini oshirmasdan qo‘shiladi.

6. Factory Method (Simple Factory) — core/factory/factory.py

Intent:
Obyekt yaratish logikasini markazlashtirish.

Implementation:

ModuleFactory.create_module(name) modul nomiga qarab tegishli subsystem’ni qaytaradi.

Amaliy jihatdan Simple Factory bo‘lsa-da, Factory Method g‘oyasini ko‘rsatadi.

Code reference:
Umarxon Muxsinov/core/factory/factory.py

Why it matters:
Yangi modul qo‘shish faqat factory’ni kengaytirish bilan amalga oshiriladi.

System Flow Summary

main.py → foydalanuvchi bilan muloqot

Controller → yagona kirish nuqtasi (Facade)

Lighting → Composite + Decorator

Weather → Adapter

Traffic → Builder

Security & Energy → mustaqil subsistemalar

Extensibility Guidelines

Yangi modul qo‘shish: modules/ ostida subsystem yaratish va Factory/Controller’da ro‘yxatdan o‘tkazish.

Weather provider almashtirish: yangi provider + adapter qo‘shish kifoya.

Lighting kengaytirish: yangi Light implementatsiyasi Composite bilan avtomatik ishlaydi.

Traffic murakkablashtirish: TrafficBuilder’ga yangi bosqichlar qo‘shiladi.

Author Information

Prepared by: Umarxon Muxsinov
Role: Developer — Architecture & Implementation
Focus: Klassik Design Pattern’larni yagona va mantiqiy SmartCity simulyatsiyasida qo‘llash