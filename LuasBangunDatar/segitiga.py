# NAMA  = HENDRA USMAN
# NIM   = D0221079
# KELAS = F - INFORMATIKA

def line():
    print("="*50)

line()
print(" MENGHITUNG LUAS SEGITIGA ".center(50,"-"))
alas_segitiga = int(input("Masukkan Panjang Alas Segitiga: "))
tinggi_segitiga = int(input("Masukkan Tinggi Segitiga: "))
luas_segitiga = 1/2 * alas_segitiga * tinggi_segitiga
print("Luas Segitiga: ", luas_segitiga, " cm²")
line()