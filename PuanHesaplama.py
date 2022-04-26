class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif

class Soru:
    def NetSayisi(self, dogruSayisi, yanlisSayisi):
        return dogruSayisi - int(yanlisSayisi / 4)

    def Hesapla(self, netSayisi):
        return netSayisi * 2

def main():
    ogrenciBilgileri = {
        'Ad': '',
        'Soyad': '',
        'Sinif': ''
    }

    denemeBilgileri = {
        'dogruSayisi': 0,
        'yanlisSayisi': 0
    }

    print('Ogrenci Bilgilerini Giriniz:')

    for keyName in ogrenciBilgileri.keys():
         ogrenciBilgileri[keyName] = input(keyName + ':')

    ogrenci = Ogrenci(ogrenciBilgileri['Ad'], ogrenciBilgileri['Soyad'], ogrenciBilgileri['Sinif'])

    print('Deneme Bilgilerini Giriniz:')

    for keyName in denemeBilgileri.keys():
         denemeBilgileri[keyName] = int(input(keyName + ':'))

    soru = Soru()

    netSayisi = soru.NetSayisi(denemeBilgileri['dogruSayisi'], denemeBilgileri['yanlisSayisi'])
    puan = soru.Hesapla(netSayisi)

    print(
        '---------------------------------------------\n' +
        'Sonuc:\n' +
        'Ad:' + ogrenci.ogrenciAdi + '\n' +
        'Soyad:' + ogrenci.ogrenciSoyadi + '\n' +
        'Sınıf:' + ogrenci.ogrenciSinif + '\n' +
        'Puan:' + str(puan)
    )

main()