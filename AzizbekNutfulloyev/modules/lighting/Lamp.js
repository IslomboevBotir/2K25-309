// modules/lighting/Lamp.js
class Lamp {
    constructor(id, type = "LED") {
        this.id = id;
        this.type = type;
        this.isOn = false;
    }

    toggle() {
        this.isOn = !this.isOn;
        console.log(`💡 Lamp ${this.id}: ${this.isOn ? "ON" : "OFF"}`);
    }
}

module.exports = Lamp;
