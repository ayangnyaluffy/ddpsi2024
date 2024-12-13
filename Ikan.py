from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan,  hidup, berkembang_biak, sirip, alat_bernafas):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.sirip = sirip
        self.alat_bernarfas = alat_bernafas

    def berenang(self):
        print(f"{self.nama} sedang berenang di {self.hidup} menggunakan sirip {self.sirip}",
              "\n-------------------------------")

    def bernafas(self):
        print(f"{self.nama} bernapas menggunakan {self.alat_bernarfas}",               
              "\n-------------------------------")

    def cetak_ikan(self):
        super().cetak()
        print("sirip \t\t\t: ", self.sirip,
              "\nalat bernafas \t\t: ", self.alat_bernarfas)

