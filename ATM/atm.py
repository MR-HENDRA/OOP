user_id = 0
loop = "n"
users = [
    {
        "id": "1234",
        "no_rekening": "1234567890",
        "username": "hendra",
        "pin": "4321",
        "saldo": 10000000
    },
    {
        "id": "4321",
        "no_rekening": "0987654321",
        "username": "usman",
        "pin": "1234",
        "saldo": 25000000
    }
]
status_login = False
pakai_atm = "y"

def cek_login(p):
    for user in users:
        if user['pin'] == p:
            return user
    return False

def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return -1

def cek_rekening(no):
    for i in range(len(users)):
        if str(users[i]['no_rekening']) == str(no):
            return int(i)
    return -1


def tranfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            users[index2]['saldo'] = users[index2]['saldo'] + int(uang)
            print("Anda Berhasil Mentransfer Uang Rp." + str(uang) + " Ke Rekening " + no_rekening)
            print("Sisa Saldo Anda Adalah Rp.", users[index1]['saldo'])
        else:
            print("Saldo Anda Tidak Cukup")

def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            print("Anda Berhasil Menarik Uang Rp." + str(uang))
            print("Sisa Saldo Anda Adalah Rp.", users[index1]['saldo'])
        else:
            print("Saldo Anda Tidak Cukup")

while pakai_atm == "y":
    while not status_login:
        print("--- SELAMAT DATANG DI ATM BANK UNSULBAR ---")
        print("Silahkan Masukan PIN Anda")
        pin = input("Masukan PIN : ")

        cl = cek_login(pin)
        if cl:
            print("Selamat Datang " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("PIN Anda Salah")
            print("")
            print("")

    while loop == "y" and status_login:
        u = users[cek_user(user_id)]
        print("--- SELAMAT DATANG DI ATM BANK UNSULBAR ---")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo Anda Adalah Rp.", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)
 
            if cnk >= 0:
                print("Nomor Rekening Ditemukan, Silahkan Masukan Nominal Yang Akan Ditransfer")
                nominal = input("Nominal Yang Akan Ditransfer : ")
                tranfer_uang(nominal, no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak Ditemukan Atau Tidak Terdaftar")
                print("")
                loop = "n"
 
        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
 
        elif a == 5:
            print("Terimakasih Telah Menggunakan ATM BANK UNSULBAR")
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("Pilihan Tidak Tersedia")
        if status_login == True:
            input("Kembali Ke Menu (Enter) ")
            print("")
            loop = "y"