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


# Instansiasi objek luas dan volume
luas = Luas(4, 6, 8, 10) # sisi, alas, tinggi, jari_jari
volume = Volume(4, 6, 8, 12, 10) # sisi, alas, tinggi, tinggi_limas, jari-jari


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
                print("Luas persegi: ", luas.hitung_luas_persegi())
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 2:
                print("Luas segitiga: ", luas.hitung_luas_segitiga())
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 3:
                print("Luas lingkaran: ", luas.hitung_luas_lingkaran())
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
                print("Volume kubus: ", volume.hitung_volume_kubus())
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 2:
                print("Volume limas segitiga: ", volume.hitung_volume_limas_segitiga())
                print(" ")
                print(input("Tekan Tombol Apapun Untuk Lanjut"))
            elif subpilihan == 3:
                print("Volume tabung: ", volume.hitung_volume_tabung())
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