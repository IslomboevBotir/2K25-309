// modules/lighting/LightingSystem.js
const Lamp = require("./Lamp");

class LightingSystem {
    constructor() {
        this.lamps = {};
    }

    addLamp(lamp) {
        this.lamps[lamp.id] = lamp;
    }

    getLamp(id) {
        return this.lamps[id];
    }

    /**
     * Factory Method:
     * Turli lampalarni yaratish
     */
    createLamp(type, id) {
        return new Lamp(id, type);
    }
}

module.exports = LightingSystem;
