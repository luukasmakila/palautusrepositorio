from kivipapreisakset import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = Tekoaly()
    
    def _toisen_siirto(self):
        return self.tekoaly.anna_siirto()