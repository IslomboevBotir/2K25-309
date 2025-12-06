// core/proxy/AuthProxy.js
class AuthProxy {
    constructor(user) {
        this.user = user;
    }

    /**
     * Proxy:
     * Faqat admin foydalanuvchi tizimni boshqara oladi
     */
    canControl(system) {
        return this.user.role === "admin";
    }
}

module.exports = AuthProxy;
