# core/proxy/security_proxy.py

class AccessDeniedError(Exception):
    """Foydalanuvchi ruxsatsiz himoyalangan amalni bajarishga urinsa, shu xatolik chiqadi."""
    pass


class SecurityProxy:
    """
    Pattern: Proxy (Struktural)

    Maqsad:
    Xavfsizlik tizimiga kirishni boshqarish.
    Masalan: faqat admin tokeni bilan tizimni qulfga tushirish yoki qulfdan chiqarish mumkin.

    Nima uchun Proxy?
    - Avtorizatsiya (ruxsat) logikasini xavfsizlik tizimining o‘ziga aralashtirmaslik uchun.
    - Proxy darvozabon sifatida ishlaydi: ruxsatni tekshiradi va haqiqiy obyektga uzatadi.
    """

    def __init__(self, real_security):
        self._real_security = real_security

    def _is_admin(self, token: str) -> bool:
        return (token or "").strip() == "admin"

    def arm(self, token: str) -> str:
        if not self._is_admin(token):
            raise AccessDeniedError("Access denied: invalid admin token.")
        return self._real_security.arm()

    def disarm(self, token: str) -> str:
        if not self._is_admin(token):
            raise AccessDeniedError("Access denied: invalid admin token.")
        return self._real_security.disarm()

    def raise_alert(self, message: str) -> str:
        # Ogohlantirish yuborish uchun admin tokeni shart emas (qoidangizga qarab)
        return self._real_security.raise_alert(message)

    def status(self) -> str:
        return self._real_security.status()
