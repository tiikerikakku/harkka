import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_1(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_2(self):
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)

    def test_3(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_4(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(50), 50)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_5(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(550), 150)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_6(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(50), 50)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_7(self):
        k = Maksukortti(500)
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(k))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_8(self):
        k = Maksukortti(50)
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(k))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(k.saldo, 50)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_9(self):
        k = Maksukortti(500)
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(k))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_10(self):
        k = Maksukortti(50)
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(k))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(k.saldo, 50)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_11(self):
        k = Maksukortti(500)
        self.kassa.lataa_rahaa_kortille(k, 500)
        
        self.assertEqual(k.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)

    def test_12(self):
        k = Maksukortti(500)
        self.kassa.lataa_rahaa_kortille(k, -500)

        self.assertEqual(k.saldo, 500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_13(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
