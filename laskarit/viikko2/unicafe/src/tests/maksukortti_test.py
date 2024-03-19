import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
    
    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    # Kortin saldo alussa oikein
    def test_kortin_saldo_asetetaan_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    # Rahan lataaminen kasvattaa saldoa oikein
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")
        
    # Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def saldo_ei_vahene_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
      
    # Saldo vähenee oikein, jos rahaa on tarpeeksi    
    def saldo_vahenee_oikein_jos_on_rahaa(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        
        
    # Metodi palauttaa True, jos rahat riittivät ja muuten False
    def test_metodi_palauttaa_oikean_arvon_maksun_onnistuessa(self):
        arvo = self.maksukortti.ota_rahaa(500)
        self.assertTrue(arvo)
        
    def test_metodi_palauttaa_oikean_arvon_maksun_epäonnistuessa(self):
        arvo = self.maksukortti.ota_rahaa(1500)
        self.assertFalse(arvo)
            

