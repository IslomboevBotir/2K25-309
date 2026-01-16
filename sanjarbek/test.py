# test.py

import unittest

from core.controller import SmartCityController
from core.factories.city_factory import BasicCityFactory
from core.proxy.security_proxy import AccessDeniedError


class AqlliShaharTizimiTest(unittest.TestCase):
    def setUp(self):
        # Har bir test uchun boshqaruvchi (controller) obyektini yaratamiz
        self.boshqaruvchi = SmartCityController(factory=BasicCityFactory())

    def test_bitta_boshqaruvchi(self):
        # Controller har doim bitta obyekt bo'lishini tekshiramiz
        c1 = SmartCityController(factory=BasicCityFactory())
        c2 = SmartCityController(factory=BasicCityFactory())
        self.assertIs(c1, c2)

    def test_transport_yuborish(self):
        # Transport marshruti yuborilishini tekshiramiz
        xabar = self.boshqaruvchi.transport_dispatch("A1")
        self.assertIn("dispatched", xabar.lower())

    def test_transport_bosh_marshrut(self):
        # Bo'sh marshrut yuborilsa, xatolik chiqishini tekshiramiz
        xabar = self.boshqaruvchi.transport_dispatch("   ")
        self.assertIn("cannot be empty", xabar.lower())

    def test_yoruglik_to_gri_qiymat(self):
        # Yorug'lik darajasi to'g'ri o'zgarganini tekshiramiz
        xabar = self.boshqaruvchi.lighting_set_brightness(80)
        self.assertIn("brightness", xabar.lower())
        self.assertEqual(self.boshqaruvchi.lighting.brightness, 80)

    def test_yoruglik_notogri_oraliq(self):
        # Yorug'lik darajasi noto'g'ri oraliqda bo'lsa, xatolik chiqishini tekshiramiz
        xabar = self.boshqaruvchi.lighting_set_brightness(150)
        self.assertIn("0-100", xabar)

    def test_energiya_tejash_rejimi(self):
        # Energiya tejash rejimi yoqilishi va o'chirilishini tekshiramiz
        xabar_on = self.boshqaruvchi.energy_enable_saving_mode()
        self.assertTrue(self.boshqaruvchi.energy.saving_mode)
        self.assertIn("enabled", xabar_on.lower())

        xabar_off = self.boshqaruvchi.energy_disable_saving_mode()
        self.assertFalse(self.boshqaruvchi.energy.saving_mode)
        self.assertIn("disabled", xabar_off.lower())

    def test_xavfsizlik_ruxsat_yoq(self):
        # Noto'g'ri token bilan xavfsizlik tizimi ishlamaganini tekshiramiz
        with self.assertRaises(AccessDeniedError):
            self.boshqaruvchi.security_arm(token="wrong-token")

    def test_xavfsizlik_ruxsat_bor(self):
        # To'g'ri (admin) token bilan xavfsizlik tizimi ishlashini tekshiramiz
        xabar = self.boshqaruvchi.security_arm(token="admin")
        self.assertIn("armed", xabar.lower())

    def test_obhavo_energiyani_yangilaydi(self):
        # Ob-havo yangilansa, energiya moduli ham yangilanishini tekshiramiz
        oldi = self.boshqaruvchi.energy.last_weather_info
        xabar = self.boshqaruvchi.sync_weather()
        yangi = self.boshqaruvchi.energy.last_weather_info

        self.assertIn("weather synced", xabar.lower())
        self.assertNotEqual(oldi, yangi)

    def test_hisobotda_barcha_bolimlar(self):
        # Hisobotda barcha bo'limlar borligini tekshiramiz
        hisobot = self.boshqaruvchi.generate_report().lower()
        self.assertIn("transport", hisobot)
        self.assertIn("lighting", hisobot)
        self.assertIn("energy", hisobot)
        self.assertIn("security", hisobot)
        self.assertIn("end of report", hisobot)


if __name__ == "__main__":
    unittest.main(verbosity=2)
