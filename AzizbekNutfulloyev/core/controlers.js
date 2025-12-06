// singleton pattern + facade pattern + proxy pattern
const LightingFactory = require("./factories/LightingFactory");
const AuthProxy = require("./proxy/AuthProxy");

class Controller {
    constructor(user) {
        if (Controller.instance) return Controller.instance; // Singleton

        this.user = user;
        this.auth = new AuthProxy(user);

        // Facade – subsistemalarga umumiy kirish
        this.lighting = new LightingFactory().createLightingSystem();

        Controller.instance = this;
    }

    toggleLight(id) {
        if (!this.auth.canControl("lighting")) {
            console.log("❌ Ruxsat yo‘q!");
            return;
        }

        const lamp = this.lighting.getLamp(id);
        if (!lamp) return console.log("Lamp topilmadi!");

        lamp.toggle();
    }
}

module.exports = Controller;
