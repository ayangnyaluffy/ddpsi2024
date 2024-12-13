from Burung import *
from Ikan import *
from ular import *

#ciptakan objek
burung1 = Burung("Merpati", "biji-bijian", "udara", "bertelur", "abu-abu", "runcing sedikit melengkung")
burung2 = Burung("Elang", "Daging", "udara", "bertelur", "Hitam", "bengkok dan tajam")

ikan1 = Ikan("Lumba-lumba", "Udang", "air laut", "Melahirkan", "Dorsal", "Paru-paru")
ikan2 = Ikan("Hiu", "Ikan kecil", "air laut", "ovovivipar", "Besar", "Insang")

ular1 = Ular("piton", "sapi", "darat", "bertelur", "macan tutul", "beracun")
ular2 = Ular("sawah", "Tikus", "darat", "bertelur", "batik", "tidak berbisa")

#print
burung1.cetak_burung()
burung2.cetak_burung()

ikan1.cetak_ikan()
ikan1.bernafas()
ikan2.cetak_ikan()
ikan2.berenang()

ular1.cetak_ular()
ular2.cetak_ular()
