from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_bulu, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_bulu = warna_bulu
        self.paruh = paruh

    def makan(self):
        print(f"{self.nama} sedang makan {self.makanan} menggunakan paruhnya yang {self.paruh}")

    def cetak_burung(self):
        super().cetak()
        print("warna_bulu \t\t: ", self.warna_bulu,
              "\nparuh \t\t\t: ", self.paruh,
              "\n-------------------------------")
        
