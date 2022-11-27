import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_tavaroita_korissa(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        tuote = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_on_sama_kuin_tuotteen(self):
        tuote = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        sipsit = Tuote("sipsit", 3)
        tacot = Tuote("tacot", 5)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(tacot)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_hinta_on_sama_kuin_tuotteiden_summa(self):
        sipsit = Tuote("sipsit", 3)
        tacot = Tuote("tacot", 5)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(tacot)

        self.assertEqual(self.kori.hinta(), 8)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(sipsit)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_on_2x_tuote(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(sipsit)

        self.assertEqual(self.kori.hinta(), 2 * sipsit.hinta())
