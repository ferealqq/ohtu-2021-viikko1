import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_kaik(self):
        self.varasto.ota_varastosta(1000)

        self.assertAlmostEqual(self.varasto.saldo,0)

    def test_lisaa_max(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus+3)

        self.assertAlmostEqual(self.varasto.saldo,self.varasto.tilavuus)

    def test_ota_nolla(self):
        d = self.varasto.ota_varastosta(0)

        self.assertAlmostEqual(d,0.0)

    def test_lisaa_nolla(self):
        o = self.varasto.saldo

        self.varasto.lisaa_varastoon(0)

        self.assertAlmostEqual(o,self.varasto.saldo)


    def test_neg_lisaa_vara(self):
        o = self.varasto

        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEquals(o,self.varasto)

    def test_neg_ota_vara(self):
        self.assertEqual(0.0,self.varasto.ota_varastosta(-1))

    def test_str(self):
        s = self.varasto.__str__()
        a = "saldo = 0, vielä tilaa 10"

        self.assertEqual(s,a)

    def test_konstrukt_iso_saldo(self):
        v = Varasto(3,100)

        self.assertEqual(3, v.saldo)

    def test_neg_konst_saldo(self):
        v = Varasto(100,-1)

        self.assertEqual(0,v.saldo)

    def test_neg_konst_tilavuus(self):
        v = Varasto(-1,3)

        self.assertEqual(0,v.tilavuus)
