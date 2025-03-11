import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein_2(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(self.kortti.saldo_euroina(), 150.0)

    def test_1(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_2(self):
        self.kortti.lataa_rahaa(-1000)

        self.assertEqual(self.kortti.saldo_euroina(), 10.0)

    def test_3(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)

    def test_4(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)
