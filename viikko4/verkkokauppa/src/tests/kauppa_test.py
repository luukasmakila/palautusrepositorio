import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 2
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "sipsit", 3)
            if tuote_id == 2:
                return Tuote(2, "burger", 8)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostoksen_paatyttya_tilisiirto_kutsutaan_oikeilla_args(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", ANY, "12345", ANY, 5)
    
    def test_kutsutaan_kahdella_eri_tuotteella_ja_oikeilla_args(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", ANY, "12345", ANY, 8)
    
    def test_lisataan_kaksi_samaa_tuotetta_ja_oikeilla_args(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", ANY, "12345", ANY, 10)

    def test_lisaa_tuote_joka_on_loppu_ja_varmista_args(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", ANY, "12345", ANY, 5)
    
    def test_aloita_asiointi_nollaa_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", ANY, "12345", ANY, 5)

        # Uusi ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", ANY, "12345", ANY, 3)
    
    def test_uusi_viitenumero_jokaiselle_tapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", 42, "12345", ANY, 5)

        # Uusi viitenumero
        self.viitegeneraattori_mock.uusi.return_value = 1
        
        # Uusi tapahtuma
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("luke", 1, "12345", ANY, 5)
    
    def test_poista_tuote_ostoskorista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("luke", "12345")
        self.pankki_mock.tilisiirto_assert_called_with("luke", ANY, "12345", ANY, 5)