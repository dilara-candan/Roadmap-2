class Insan:
    def __init__(self):
        self.ad = 'Dilara'
        self.soyad = 'Candan'
        self.yas = 25
        self.ulke = 'Türkiye'
        self.sehir = 'Erzurum'
        self.yetenekler = ['Python', 'Bisiklet Binmek']

    def kisi_bilgileri(self):
        print(self.__dict__)

    def yetenek_ekle(self, yetenekAdi):
        if (type(yetenekAdi) is list):
            self.yetenekler.extend(yetenekAdi)
        else:
            self.yetenekler.append(yetenekAdi)

def main():
    insan = Insan()

    insan.yetenek_ekle('Araba Sürmek')
    insan.yetenek_ekle('At Binmek')

    # Veya

    insan.yetenek_ekle(['C++', 'JavaScript'])

    insan.kisi_bilgileri()

main()
