from person import *
class Dosen(person):
    #pass jika tidak ada tambahan property dan method lainnya
    gelar = ""
    jabatan = ""
    gaji = 0
    def __init__(self, nama, gender, umur, gelar, jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
    def setGaji(self, uang):
        self.gaji += uang
    def cetak(self):
        super().cetak()
        print("gelar \t\t: ", self.gelar,
              "\njabatan \t: ", self.jabatan,
              "\ngaji \t\t: ", self.gaji,
              "\n-------------------------------")
    