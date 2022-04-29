class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif

class Soru(Ogrenci):
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        super().__init__(ogrenciAdi, ogrenciSoyadi, ogrenciSinif)

    def NetSayisi(self, dogruSayisi, yanlisSayisi):
        if (dogruSayisi + yanlisSayisi > 50):
            print("50 soru sınırırı geçtiniz.")
            return

        return dogruSayisi - int(yanlisSayisi / 4)

    def Hesapla(self, netSayisi):
        if (type(netSayisi) == int):
            print(
                '---------------------------------------------\n' +
                'Sonuc:\n' +
                'Ad:' + self.ogrenciAdi + '\n' +
                'Soyad:' + self.ogrenciSoyadi + '\n' +
                'Sınıf:' + self.ogrenciSinif + '\n' +
                'Puan:' + str(netSayisi * 2)
            )

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

soru = Soru(ogrenci.ogrenciAdi, ogrenci.ogrenciSoyadi, ogrenci.ogrenciSinif)
netSayisi = soru.NetSayisi(int(denemeBilgileri['dogruSayisi']), int(denemeBilgileri['yanlisSayisi']))

soru.Hesapla(netSayisi)
