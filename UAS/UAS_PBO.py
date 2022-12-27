# NAMA  : HENDRA USMAN
# NIM   : D0221079
# KELAS : INFORMATIKA - F

# CLASS LUAS
class Luas:
  def __init__(self, sisi, alas, tinggi, jari_jari):
    self.sisi = sisi
    self.alas = alas
    self.tinggi = tinggi
    self.jari_jari = jari_jari

  def hitung_luas_persegi(self):
    rumus_luas_persegi = self.sisi * self.sisi
    print("Luas Persegi : ", rumus_luas_persegi)

  def hitung_luas_segitiga(self):
    rumus_luas_segitiga = self.alas * self.tinggi / 2
    print("Luas Segitiga :", rumus_luas_segitiga)

  def hitung_luas_lingkaran(self):
    rumus_luas_lingkaran = 22/7 * self.jari_jari * self.jari_jari
    print("Luas Lingkaran :", rumus_luas_lingkaran)

# CLASS VOLUME
class Volume:
  def __init__(self, sisi, alas, tinggi, tinggi_limas, jari_jari):
    self.sisi = sisi
    self.alas = alas
    self.tinggi = tinggi
    self.tinggi_limas = tinggi_limas
    self.jari_jari = jari_jari

  def hitung_volume_kubus(self):
    rumus_volume_kubus = self.sisi * self.sisi * self.sisi
    print("Volume Kubus : ", rumus_volume_kubus)

  def hitung_volume_limas_segitiga(self):
    rumus_volume_limas_segitiga = 1/3 * ((1/2 * self.alas * self.tinggi) * self.tinggi_limas)
    print("Volume Limas Segitiga : ", rumus_volume_limas_segitiga)
    
  def hitung_volume_tabung(self):
    rumus_volume_tabung = 22/7 * self.jari_jari * self.jari_jari * self.tinggi
    print("Volume Tabung : ", rumus_volume_tabung)

# MENU
while True:
    print(" ")
    print("=" * 50)
    print(" PROGRAM MENGHITUNG LUAS DAN VOLUME ".center(50,"="))
    print("=" * 50)
    print("\n1. Luas \n2. Volume \n3. Keluar")
    pilihan = int(input("\nMasukkan Pilihan : "))
    if pilihan == 1:
        while True:
            print(" ")
            print("=" * 50)
            print(" PROGRAM MENGHITUNG LUAS ".center(50, "="))
            print("=" * 50)
            print("\n1. Persegi \n2. Segitiga \n3. Lingkaran \n4. Kembali")
            subpilihan = int(input("\nMasukkan Pilihan : "))
            if subpilihan == 1:
                print(" ")
                print("-" * 50)
                print(" PROGRAM MENGHITUNG LUAS PERSEGI ".center(50,"="))
                print("-" * 50)
                sisi = float(input("Masukkan Sisi Persegi : "))
                luas_persegi = Luas(sisi, 0, 0, 0)
                Luas.hitung_luas_persegi(luas_persegi)
                print("-" * 50)
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
            elif subpilihan == 2:
                print(" ")
                print("-" * 50)
                print(" PROGRAM MENGHITUNG LUAS SEGITGA ".center(50,"="))
                print("-" * 50)
                alas = float(input("Masukkan Alas Segitiga : "))
                tinggi = float(input("Masukkan Tinggi Segitiga : "))
                luas_segitiga = Luas(0, alas, tinggi, 0)
                Luas.hitung_luas_segitiga(luas_segitiga)
                print("-" * 50)
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
            elif subpilihan == 3:
                print(" ")
                print("-" * 50)
                print(" PROGRAM MENGHITUNG LUAS LINGKARAN ".center(50,"="))
                print("-" * 50)
                jari_jari = float(input("Masukkan Jari-Jari Lingkaran : "))
                luas_lingkaran = Luas(0, 0, 0, jari_jari)
                Luas.hitung_luas_lingkaran(luas_lingkaran)
                print("-" * 50)
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
            elif subpilihan == 4:
                break
            else:
                print("Perintah Tidak Ditemukan")
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
                
    elif pilihan == 2:
        while True:
            print(" ")
            print("=" * 50)
            print(" PROGRAM MENGHITUNG VOLUME ".center(50, "="))
            print("=" * 50)
            print("\n1. Kubus \n2. Limas Segitiga \n3. Tabung \n4. Kembali")
            subpilihan = int(input("\nMasukkan Pilihan : "))
            if subpilihan == 1:
                print(" ")
                print("-" * 50)
                print(" PROGRAM MENGHITUNG VOLUME KUBUS ".center(50,"="))
                print("-" * 50)
                sisi = float(input("Masukkan panjang sisi : "))
                volume_segitiga = Volume(sisi, 0, 0, 0, 0)
                Volume.hitung_volume_kubus(volume_segitiga)
                print("-" * 50)
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
            elif subpilihan == 2:
                print(" ")
                print("-" * 50)
                print(" PROGRAM MENGHITUNG VOLUME LIMAS SEGITIGA ".center(50,"="))
                print("-" * 50)
                alas = float(input("Masukkan nilai alas : "))
                tinggi = float(input("Masukkan  nilai tinggi : "))
                tinggi_limas = float(input("Masukkan tinggi limas : "))
                volume_limas_segitiga = Volume(0, alas, tinggi, tinggi_limas, 0)
                Volume.hitung_volume_limas_segitiga(volume_limas_segitiga)
                print("-" * 50)
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
            elif subpilihan == 3:
                print(" ")
                print("-" * 50)
                print(" PROGRAM MENGHITUNG VOLUME TABUNG ".center(50,"="))
                print("-" * 50)
                jari_jari = float(input("Masukkan Jari-Jari Lingkaran Tabung : "))
                tinggi = float(input("Masukkan Tinggi Tabung : "))
                volume_tabung = Volume(0, 0, tinggi, 0, jari_jari)
                Volume.hitung_volume_tabung(volume_tabung)
                print("-" * 50)
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
            elif subpilihan == 4:
                break
            else:
                print("Perintah Tidak Ditemukan")
                print(" ")
                print(input("Tekan Enter Untuk Lanjut"))
    elif pilihan == 3:
        print(" ")
        print("-" * 50)
        print(" EXIT PROGRAM ".center(50,"="))
        print("-" * 50)
        break
    else:
        print("Perintah Tidak Ditemukan")
        print(" ")
        print(input("Tekan Enter Untuk Lanjut"))