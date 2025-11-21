const LightingSystem = require("../../modules/lighting/LightingSystem");

class LightingFactory {

    createLightingSystem() {
        const system = new LightingSystem();

        system.addLamp(system.createLamp("LED", "L1"));
        system.addLamp(system.createLamp("Halogen", "L2"));

        return system;
    }
}

module.exports = LightingFactory;
