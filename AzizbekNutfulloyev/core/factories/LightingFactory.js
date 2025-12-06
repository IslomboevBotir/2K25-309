// core/factories/LightingFactory.js
const LightingSystem = require("../../modules/lighting/LightingSystem");

class LightingFactory {
    /**
     * Abstract Factory:
     * Butun yoritish tizimini yaratadi
     */
    createLightingSystem() {
        const system = new LightingSystem();

        // Factory Method orqali lampalar yaratish
        system.addLamp(system.createLamp("LED", "L1"));
        system.addLamp(system.createLamp("Halogen", "L2"));

        return system;
    }
}

module.exports = LightingFactory;
