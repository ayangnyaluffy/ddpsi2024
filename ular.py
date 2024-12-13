from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Corak \t\t\t: ", self.corak,
              "\nracun \t\t\t: ", self.racun,
              "\n-------------------------------")
        
