def line():
    print("="*50)

line()
print(" MENGHITUNG LUAS LINGKARAN ".center(50,"-"))
jari_jari = int(input("Masukkan Panjang Jari-Jari Lingkaran: "))
luas_lingkaran = 3.14 * jari_jari ** 2
print("Luas Lingkaran: ", luas_lingkaran, " cm²")
line()