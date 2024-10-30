pilihan = int(input("""pilih nomor pilihan :  
                1. menghitung luas persegi 
                2. menghitung luas lingkaran 
                3. menghitung luas segitiga"""))
match pilihan:
    case 1:
        print("menghitung luas persegi")
        s = int(input("masukkan nilai sisi: "))
        luaspersegi = s * s
        print(f"luas persegi dengan sisi {s} adalah {luaspersegi}")
    case 2:
        print("menghitung luas lingkaran")
        pi = 3.14
        r = int(input("masukkan nilai jari-jari"))
        luaslingkaran = pi * r** 2
        print(f"luas lingkaran dengan jari jari {r} adalah {luaslingkaran}") 
    case 3:
        print("menghitung luas segitiga")
        alas = int(input("masukkan nilai alas: "))
        tinggi = int(input("masukkan nilai tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
    case _:
        print("input tidak valid")
        