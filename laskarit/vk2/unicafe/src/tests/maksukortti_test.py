import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_1(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_2(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_3(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 500)

    def test_4(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_5(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_6(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1500))

    def test_7(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')

    def test_8(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
