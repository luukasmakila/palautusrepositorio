from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto in ("k", "p", "s")