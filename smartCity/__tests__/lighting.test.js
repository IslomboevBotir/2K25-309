const Lamp = require("../modules/lighting/Lamp");
const LightingSystem = require("../modules/lighting/LightingSystem");
const LightingFactory = require("../core/factories/LightingFactory");
const Controller = require("../core/controlers");
const AuthProxy = require("../core/proxy/AuthProxy");


describe("Lamp", () => {
  test("Lamp initial state is OFF", () => {
    const lamp = new Lamp("L1");
    expect(lamp.isOn).toBe(false);
  });

  test("Lamp toggle changes state", () => {
    const lamp = new Lamp("L1");
    lamp.toggle();
    expect(lamp.isOn).toBe(true);
    lamp.toggle();
    expect(lamp.isOn).toBe(false);
  });
});

describe("LightingSystem", () => {
  test("Factory Method creates lamp correctly", () => {
    const system = new LightingSystem();
    const lamp = system.createLamp("LED", "L1");
    expect(lamp.type).toBe("LED");
    expect(lamp.id).toBe("L1");
  });

  test("Add and get lamp works", () => {
    const system = new LightingSystem();
    const lamp = system.createLamp("LED", "L1");
    system.addLamp(lamp);
    expect(system.getLamp("L1")).toBe(lamp);
  });
});

describe("LightingFactory", () => {
  test("Factory creates system with 2 lamps", () => {
    const factory = new LightingFactory();
    const system = factory.createLightingSystem();
    expect(Object.keys(system.lamps).length).toBe(2);
    expect(system.lamps["L1"]).toBeDefined();
    expect(system.lamps["L2"]).toBeDefined();
  });
});

describe("AuthProxy", () => {
  test("Admin can control", () => {
    const proxy = new AuthProxy({ role: "admin" });
    expect(proxy.canControl("lighting")).toBe(true);
  });

  test("Guest cannot control", () => {
    const proxy = new AuthProxy({ role: "guest" });
    expect(proxy.canControl("lighting")).toBe(false);
  });
});

describe("Controller Singleton", () => {
  test("Controller is singleton", () => {
    const user1 = { name: "A", role: "admin" };
    const user2 = { name: "B", role: "admin" };
    const c1 = new Controller(user1);
    const c2 = new Controller(user2);
    expect(c1).toBe(c2);
  });
});
