class person:
    nama = ""
    gender = ""
    umur = ()

    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur

    def cetak(self):
        print("nama \t\t: ", self.nama,
              "\ngender \t\t: ", self.gender,
              "\nUmur \t\t: ", self.umur)