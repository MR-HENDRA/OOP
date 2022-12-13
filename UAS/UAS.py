# menggunakan inputan user tapi masih error dalam eksekusi perintah
# option kembali dan keluar sudah berfungsi dengan baik

class Luas:
  def __init__(self, sisi, alas, tinggi, jari_jari):
    self.sisi = sisi
    self.alas = alas
    self.tinggi = tinggi
    self.jari_jari = jari_jari

  def hitung_luas_persegi(self):
    return self.sisi * self.sisi

  def hitung_luas_segitiga(self):
    return self.alas * self.tinggi / 2

  def hitung_luas_lingkaran(self):
    return 3.14 * self.jari_jari * self.jari_jari

class Volume:
  def __init__(self, sisi, alas, tinggi, tinggi_limas, jari_jari):
    self.sisi = sisi
    self.alas = alas
    self.tinggi = tinggi
    self.tinggi_limas = tinggi_limas
    self.jari_jari = jari_jari

  def hitung_volume_kubus(self):
    return self.sisi * self.sisi * self.sisi

  def hitung_volume_limas_segitiga(self):
    return 1/3 * ((1/2 * self.alas * self.tinggi) * self.tinggi_limas)

  def hitung_volume_tabung(self):
    return 3.14 * self.jari_jari * self.jari_jari * self.tinggi

# MENU

print("=" * 50)
print("=", "PROGRAM MENGHITUNG LUAS DAN VOLUME".center(46), "=")
print("=" * 50)
while True:
    print("\n1. Luas \n2. Volume \n3. Keluar")
    pilihan = int(input("Masukkan Pilihan : "))
    if pilihan == 1:
        while True:
            print("\n1. Persegi \n2. Segitiga \n3. Lingkaran \n4. Kembali")
            subpilihan = int(input("Masukkan Pilihan : "))
            if subpilihan == 1:
                sisi = float(input("Masukkan Sisi Persegi : "))
                hasil = Luas()
                hasil.hitung_luas_persegi()
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 2:
                alas = float(input("Masukkan Alas Segitiga : "))
                tinggi = float(input("Masukkan Tinggi Segitiga : "))
                hasil = Luas()
                hasil.hitung_luas_segitiga()
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 3:
                jari_jari = float(input("Masukkan Jari-Jari Lingkaran : "))
                hasil = Luas()
                hasil.hitung_luas_lingkaran()
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 4:
                break
            else:
                print("Perintah Tidak Ditemukan")
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
                
    elif pilihan == 2:
        while True:
            print("\n1. Kubus \n2. Limas Segitiga \n3. Tabung \n4. Kembali")
            subpilihan = int(input("Masukkan Pilihan : "))
            if subpilihan == 1:
                sisi = float(input("Masukkan panjang sisi : "))
                hasil = Volume()
                hasil.hitung_volume_kubus()
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 2:
                alas = float(input("Masukkan nilai alas : "))
                tinggi = float(input("Masukkan  nilai tinggi : "))
                tinggi_limas = float(input("Masukkan tinggi limas : "))
                hasil = Volume()
                hasil.hitung_volume_limas_segitiga()
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 3:
                jari_jari = float(input("Masukkan Jari-Jari Lingkaran Tabung : "))
                tinggi = float(input("Masukkan Tinggi Tabung : "))
                hasil = Volume()
                hasil.hitung_volume_tabung()
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 4:
                break
            else:
                print("Perintah Tidak Ditemukan")
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
    elif pilihan == 3:
        break
    else:
        print("Perintah Tidak Ditemukan")
        print(" ")
        print(input("Tekan Tombol Apapun Untuk Lanjut"))