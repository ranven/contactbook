import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        
    # Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea
    def test_kassa_alustetaan_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset+self.kassa.maukkaat, 0)
        
    # Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta 
    def test_lounaan_kateisosto_toimii_riittavalla_maksulla(self):
        maukas = self.kassa.syo_maukkaasti_kateisella(1000)
        self.assertEqual(maukas, 600)
        
        edullinen = self.kassa.syo_edullisesti_kateisella(1000)
        self.assertEqual(edullinen, 760)
        
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_lounaan_kateisosto_toimii_riittamattomalla_maksulla(self):
        edullinen = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(edullinen, 100)
        
        maukas = self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(maukas, 100)
        
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.edulliset, 0)
        
    # Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta 
    def test_lounaan_korttiosto_toimii_riittavalla_maksulla(self):
        kortti = Maksukortti(640)
        palautusarvo = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertTrue(palautusarvo)
        self.assertEqual(kortti.saldo, 400)
        
        palautusarvo = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertTrue(palautusarvo)
        self.assertEqual(kortti.saldo, 0)
        
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

        
    def test_lounaan_korttiosto_toimii_riittamattomalla_maksulla(self):
        kortti = Maksukortti(100)
        palautusarvo = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertFalse(palautusarvo)
        self.assertEqual(kortti.saldo, 100)
        
        palautusarvo = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(palautusarvo)
        self.assertEqual(kortti.saldo, 100)
        
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    #Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_kortin_lataaminen_kasvattaa_kassaa(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 1000)
        
        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortille_ei_voi_ladata_negatiivista_arvoa(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, -1000)
        
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)