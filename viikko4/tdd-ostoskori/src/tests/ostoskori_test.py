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
    
    def test_yhden_tuotteen_jalkeen_korissa_yksi_ostos(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "sipsit")
        self.assertEqual(ostos.lukumaara(), 1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tuotetta(self):
        sipsit = Tuote("sipsit", 3)
        tacot = Tuote("tacot", 5)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(tacot)

        self.assertEqual(len(self.kori.ostokset()), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_yksi_ostos(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(sipsit)

        self.assertEqual(len(self.kori.ostokset()), 1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostos_oikein(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(sipsit)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "sipsit")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_2_samaa_tuotetta_poisto_oikein(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)
        self.kori.lisaa_tuote(sipsit)

        self.kori.poista_tuote(sipsit)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)
    
    def test_koriin_lisatty_tuote_poistetaan_kori_tyhja(self):
        sipsit = Tuote("sipsit", 3)
        self.kori.lisaa_tuote(sipsit)
        self.kori.poista_tuote(sipsit)

        self.assertEqual(len(self.kori.ostokset()), 0)
