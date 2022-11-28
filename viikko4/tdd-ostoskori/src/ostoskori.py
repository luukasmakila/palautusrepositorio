from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if not self.kori: return 0

        tavaroita = 0
        for key in self.kori:
            ostos = self.kori[key]
            tavaroita += ostos.lukumaara()
        return tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if not self.kori: return 0

        hinta = 0
        for key in self.kori:
            ostos = self.kori[key]
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() not in self.kori:
            self.kori[lisattava.nimi()] = Ostos(lisattava)
            return

        self.kori[lisattava.nimi()].muuta_lukumaaraa(1)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() not in self.kori: return

        self.kori[poistettava.nimi()].muuta_lukumaaraa(-1)

        if self.kori[poistettava.nimi()].lukumaara() == 0:
            del self.kori[poistettava.nimi()]

    def tyhjenna(self):
        self.kori = {}
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return list(self.kori.values())
    #test