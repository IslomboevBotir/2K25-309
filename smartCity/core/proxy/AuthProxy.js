class AuthProxy {
    constructor(user) {
        this.user = user;
    }


    canControl(system) {
        return this.user.role === "admin";
    }
}

module.exports = AuthProxy;
