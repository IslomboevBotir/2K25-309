// main.js
const readline = require("readline");
const Controller = require("./core/controlers");

class User {
    constructor(name, role = "guest") {
        this.name = name;
        this.role = role;
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const user = new User("Azizbek", "admin");
const controller = new Controller(user);

function menu() {
    console.log(`
=== SmartCity System ===
1) Lamp L1 yoqish/o‘chirish
2) Lamp L2 yoqish/o‘chirish
q) Chiqish
`);
    rl.question(">>> ", (k) => {
        if (k === "1") controller.toggleLight("L1");
        if (k === "2") controller.toggleLight("L2");
        if (k === "q") return rl.close();

        menu();
    });
}

menu();
