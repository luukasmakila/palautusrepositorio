from kivipapreisakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self):
        return self.tekoaly.anna_siirto()