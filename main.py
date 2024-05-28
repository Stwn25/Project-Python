import csv
import pandas as pd
import os
import re
import datetime
date_time = datetime.datetime.now()

def clear():
    os.system('cls')

def sign():
    data_login.clear()
    pw_super_admin = 'superadmin'

    print(f'{'='*37}')
    print(f'|{'Lets CAMP!':^35}|')  
    print(f'{'='*37}')

    pilih = input('Halo, \nIngin login(l)/regis(r) : ')

    if pilih == 'r':
        regis()

    elif pilih == 'l':
        login()

    elif pilih == 'sa':
        pass_admin = input('Password : ')
        if pass_admin == pw_super_admin:
            clear()
            print('Berhasil masuk !')
            print('='*35)
            home_super_admin()
        else:
            print('\nPassword salah !')
            sign()

    else:
        clear()
        print('\nMasukkan input yang sesuai !')
        sign()

#============================================================================
#Login/Registrasi
#============================================================================

def regis_admin():
    print('-'*35)
    print(f'{'ADMIN':^35}')
    print('-'*35)

    status = 'admin'
    
    username = input('*Minimal 6 karakter \nUsername : ')
    if len(username) < 6:
        print('\nUsername minimal 6 karakter !')
        regis_admin()

    password = input('\n*Minimal 8 karakter, huruf kapital, symbol, dan angka \nPassword : ')
    if len(password) < 8 or not any(char.isupper() for char in password) or not re.search("[!@#$%^&*(),.?':{}|<>]", password) or not any(char.isdigit() for char in password):
        print('\nPassword tidak memenuhi syarat (minimal 8 karakter, huruf kapital, symbol, dan angka) !')
        regis_admin()
        
    
    name = input('\nNama : \n')
    if name == '':
        print('Masukkan nama !')
        regis_admin()
    
    telpon = input('\nNomor telpon : \n')
    if telpon == '':
        print('Masukkan nomor telepon !')
        regis_admin()

    data_akun =[]

    with open ('dataakun.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_akun.append({'username':row[0],'password':row[1], 'nama':row[2], 'no.telp': row[3], 'status': row[4]})

    available = False

    for akun in data_akun:
        if username == akun['username']:
            available = True
            print('\nUsername telah tersedia, coba lagi !')
            regis_admin()

    if available == False:
        new_data = {'username': username, 'password': password,'nama':name, 'no.telp': telpon, 'status': status}
        with open ('dataakun.csv', 'a', newline='') as file :
            write = csv.DictWriter(file, fieldnames=new_data.keys())
            write.writerow(new_data)
            file.flush()
            file.close()
                
            clear()
            print('\nAkun admin berhasil ditambahkan !')
            home_super_admin()

#============================================================================

def regis_customer():
    print('-'*35)
    print(f'{'CUSTOMER':^35}')
    print('-'*35)

    status = 'customer'

    username = input('*Minimal 6 karakter \nUsername : ')
    if len(username) < 6:
        print('\nUsername minimal 6 karakter !')
        regis_customer()

    password = input('\n*Minimal 8 karakter, huruf kapital, symbol, dan angka \nPassword : ')
    if len(password) < 8 or not any(char.isupper() for char in password) or not re.search("[!@#$%^&*(),.?':{}|<>]", password) or not any(char.isdigit() for char in password):
        print('\nPassword tidak memenuhi syarat (minimal 8 karakter, huruf kapital, symbol, dan angka) !')
        regis_customer()
        
    
    name = input('\nNama : \n')
    if name == '':
        print('Masukkan nama !')
        regis_customer()
    
    telpon = input('\nNomor telpon : \n')
    if telpon == '':
        print('Masukkan nomor telepon !')
        regis_customer()


    data_akun =[]

    with open ('dataakun.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_akun.append({'username':row[0],'password':row[1], 'nama':row[2], 'no.telp': row[3], 'status': row[4]})

    available = False

    for akun in data_akun:
        if username == akun['username']:
            available = True
            print('\nUsername telah tersedia, coba lagi !')
            regis_customer()

    if available == False:
        new_data = {'username': username, 'password': password,'nama':name, 'no.telp': telpon, 'status': status}
        with open ('dataakun.csv', 'a', newline='') as file :
            write = csv.DictWriter(file, fieldnames=new_data.keys())
            write.writerow(new_data)
            file.flush()
            file.close()

            clear()
            print('\nAkun customer berhasil ditambahkan !')
            sign()

#============================================================================

def regis():
    print('='*35)
    print(f'{'REGISTRASI':^35}')
    print('='*35)
    print('\n*Untuk registrasi sebagai admin, \nhubungi super admin ! \n')
    
    regis_customer()
    
        
#============================================================================

data_login = []

def login_admin():
    print('-'*37)
    print(f'|{'ADMIN':^35}|')
    print('-'*37)

    status = 'admin'
    username = input('Username : \n')
    if len(username) < 6:
        print('*Minimal 6 karakter')
        login_admin()
    password = input('Password : \n')
    if len(password) < 8:
        print('*Minimal 8 karakter, huruf kapital, symbol, dan angka') 
        login_admin()

    data_akun = []

    with open ('dataakun.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_akun.append({'username':row[0],'password':row[1], 'nama':row[2], 'no.telp': row[3], 'status': row[4]})
    
    succes = False   
    for akun in data_akun:
        if username == akun['username'] and password == akun['password'] and status == akun['status']:
            if akun['status'] == 'admin':
                data_login.append(akun)

                riwayat = {'username': data_login[0]['username'], 'password': data_login[0]['password'], 'nama': data_login[0]['nama'], 'no.telp': data_login[0]['no.telp'], 'status': data_login[0]['status'], 'riwayat': date_time}
                with open ('riwayatlogin.csv', 'a', newline='') as login:
                    write = csv.DictWriter(login, fieldnames=riwayat.keys())
                    write.writerow(riwayat)

                clear()
                print('\nBerhasil Masuk !')
                print('='*35)
                home_admin()
                succes = True
    
    if not succes:
        clear()
        print('\nUsername atau password salah, Silakan coba lagi !')
        login_admin()


#============================================================================

def login_customer():
    print('-'*35)
    print(f'{'CUSTOMER':^35}')
    print('-'*35)
    status = 'customer'
    username = input('Username : \n')
    if len(username) < 6:
        print('*Minimal 6 karakter')
        login_customer()
    password = input('Password : \n')
    if len(password) < 8:
        print('*Minimal 8 karakter, huruf kapital, symbol, dan angka') 
        login_customer()

    data_akun = []

    with open ('dataakun.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_akun.append({'username':row[0],'password':row[1], 'nama':row[2], 'no.telp': row[3], 'status': row[4]})

    succes = False
    for akun in data_akun:
        if username == akun['username'] and password == akun['password'] and status == akun['status']:
            if akun['status'] == 'customer':
                data_login.append(akun)
                
                riwayat = {'username': data_login[0]['username'], 'password': data_login[0]['password'], 'nama': data_login[0]['nama'], 'no.telp': data_login[0]['no.telp'], 'status': data_login[0]['status'], 'riwayat': date_time}
                with open ('riwayatlogin.csv', 'a', newline='') as login:
                    write = csv.DictWriter(login, fieldnames=riwayat.keys())
                    write.writerow(riwayat)

                clear()
                print('\nBerhasil Masuk !')
                print('='*35)
                home_customer()
                succes = True

       
    if not succes:
        clear()
        print('\nUsername atau password salah, Silakan coba lagi !')
        login_customer()
        # elif username != akun['username'] and password != akun['password'] and status == akun['status']:
        #     print('\nsalah input username/password !')
        #     login_customer()

        # elif username == akun['username'] and password == akun['password'] and status != akun['status']:
        #     print('\nsalah input username/password !')
        #     login_customer()
 
 #============================================================================

def login():
    print('='*37)
    print(f'|{'LOGIN':^35}|')
    print('='*37)
    print('\n[1] Admin \n[2] Customer')
    masuk = input('\nLog in sebagai (1/2) : ')

    if masuk == '1':
        login_admin()

    elif masuk == '2':
        login_customer()

    else:
        clear()
        print('\nMasukkan nomor menu yang sesuai !')
        login()
        

#============================================================================
#Akhir, Login/Registrasi
#============================================================================

#============================================================================
#Sebagai Superadmin
#============================================================================
def home_super_admin():

    pilih_menu = input(f'Selamat Datang, Super Admin !\n\n[1] Data Akun \n[2] Riwayat Login \n[3] Daftar Admin \n[4] Log Out \n\nPilih menu : ')
    

    if pilih_menu == '1':
        clear()
        lihat_akun()

    elif pilih_menu == '2':
        clear()
        print('-'*35)
        riwayat_login()

    elif pilih_menu == '3':
        clear()
        regis_admin()

    elif pilih_menu == '4':
        clear()
        sign()

    else:
        clear()
        print('\nMasukkan nomor menu yang sesuai !')
        print('='*35)
        home_super_admin()
        

#============================================================================
#Akhir sebagai Superadmin
#============================================================================

#============================================================================
#function, Superadmin
#============================================================================
def lihat_akun():
    print('='*37)
    print(f'|{'Data Akun Admin/Customer':^35}|')
    print(f'{'='*37}\n')

    data_akun = []
    with open('dataakun.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_akun.append([row[0],row[1],row[2],row[3],row[4]])

    kolom = ['username','password','nama','no.telp','status']
    df = pd.DataFrame(data_akun, columns=kolom)
    df.index += 1
    print(df)

    menu = input('\n[1] Hapus \n[2] Kembali \n\nPilih menu : ')

    if menu =='1':
        print('-'*35)
        hapus_akun()
    elif menu =='2':
        clear()
        home_super_admin()
    else:
        clear()
        print('Masukkan nomor menu yang sesuai !')
        lihat_akun()

#============================================================================

def hapus_akun():
    data_akun = []
    with open('dataakun.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_akun.append([row[0],row[1],row[2],row[3],row[4]])

    kolom = ['username','password','nama','no.telp','status']
    df = pd.DataFrame(data_akun, columns=kolom)
    df.index += 1
    print(df)

    try:
        baris_input = input('\nNomor baris yang ingin dihapus (enter = cancel) : ')
        if not baris_input:
            print('\nCancel !')
            lihat_akun()
        baris = int(baris_input)

    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        hapus_akun()

    data = 0
    for data_perbaris in range(len(data_akun)):
        if data_perbaris + 1 == baris:
            data = 1
            data_akun.pop(data_perbaris)

            with open ('dataakun.csv', 'w', newline='') as file:
                write = csv.writer(file)
                write.writerows(data_akun)

            clear()
            print('\nData akun berhasil dihapus !')
            print('='*35)
            home_super_admin()

    if data == 0:
        print('\nTidak ada data pada baris tersebut !')
        print('-'*35)
        hapus_akun()

#============================================================================

def riwayat_login():
    clear()
    print('='*37)
    print(f'|{'Riwayat Login':^35}|')
    print(f'{'='*37}\n')

    data_riwayat = []
    with open ('riwayatlogin.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_riwayat.append({'username': row[0], 'password': row[1], 'nama': row[2], 
                                 'no.telp': row[3], 'status': row[4], 'riwayat': row[5]})

    df = pd.DataFrame(data_riwayat)
    df.index += 1
    print(df)
    kembali_super_admin()

def kembali_super_admin():
    back = input('\nKembali >> (klik enter)')
    if back == '':
        clear()
        home_super_admin()
    else:
        kembali_super_admin()

#============================================================================
#Akhir function, Superadmin
#============================================================================

#============================================================================
#Sebagai Admin
#============================================================================

def home_admin():
    pilih_menu = input(f'Selamat Datang, {data_login[0]['nama']} !\n\n[1] Kelola Alat Camping \n[2] Pesanan Customer \n[3] Log Out \n\nPilih menu : ')
    clear()

    if pilih_menu == '1':
        menu_satu_admin()

    elif pilih_menu == '2':
        menu_dua_admin()

    elif pilih_menu == '3':
        sign()

    else:
        print('\nMasukkan nomor menu yang sesuai !')
        print('='*35)
        home_admin()

#============================================================================
#Menu 1 home_admin
#============================================================================

def menu_satu_admin():
    print(f'{'-'*37}')
    print(f'|{'Kelola Alat Camping':^35}|')
    print(f'{'-'*37}')
    print('\n[1] Satuan \n[2] Paketan \n[3] Kembali')
    menu = input('\nPilih menu :')
    clear()

    if menu == '1':
        pilih_satuan()
    elif menu == '2':
        pilih_paketan()
    elif menu == '3':
        print('='*35)
        home_admin()
    else:
        print('\nMasukkan nomor menu yang sesuai !')
        menu_satu_admin()

#============================================================================

def pilih_satuan():
    print(f'{'-'*37}')
    print(f'|{'Satuan':^35}|')
    print(f'{'-'*37}')
    print('\n[1] Tambah Alat \n[2] Lihat Data Alat \n[3] Update Data Alat \n[4] Hapus Data Alat \n[5] Kembali')
    pilih_submenu = input('\nPilih menu : ')

    if pilih_submenu == '1': 
        print('-'*35)
        tambah_alat()
    elif pilih_submenu == '2':
        print('-'*35)
        lihat_alat()
    elif pilih_submenu == '3':
        print('-'*35)
        update_alat()
    elif pilih_submenu == '4':
        print('-'*35)
        hapus_alat()
    elif pilih_submenu == '5':
        clear()
        menu_satu_admin()
    else:
        clear()
        print('\nMasukkan nomor menu yang sesuai !')
        pilih_satuan()

#============================================================================

def pilih_paketan():
    print(f'{'-'*37}')
    print(f'|{'Paketan':^35}|')
    print(f'{'-'*37}')
    print('\n[1] Tambah Paket \n[2] Lihat Data Paket \n[3] Update Data Paket \n[4] Hapus Data Paket \n[5] Kembali')
    pilih_submenu = input('\nPilih menu : ')

    if pilih_submenu == '1':
        print('-'*35) 
        tambah_paket()
    elif pilih_submenu == '2':
        print('-'*35)
        lihat_paket()
    elif pilih_submenu == '3':
        print('-'*35)
        update_paket()
    elif pilih_submenu == '4':
        print('-'*35)
        hapus_paket()
    elif pilih_submenu == '5':
        clear()
        menu_satu_admin()
    else:
        clear()
        print('\nMasukkan nomor menu yang sesuai !')
        pilih_paketan()
    
    
#============================================================================
#Akhir Menu 1 home_admin
#============================================================================


#============================================================================
#function, menu 1. Kelola Alat Camping
#============================================================================

#Satuan

def tambah_alat() :

    print(f'{'Tambah Alat':^35}')
    alat = input('\nNama Alat : \n')
    if alat == '':
        print('\nMasukkan nama alat !')
        print('-'*35)
        tambah_alat()

    harga = input('Harga Sewa per Hari (rp) : \n')
    if len(harga) < 3:
        print('\nMasukkan harga (dalam rupiah) !')
        print('-'*35)
        tambah_alat()

    data_alat = []

    with open ('dataalat.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_alat.append({'alat':row[0],'harga':row[1]})

    available = False

    for i in data_alat:
        if alat == i['alat']:
            available = True
            print('\nAlat Telah Di input, coba lagi !')
            print('-'*35)
            tambah_alat()

    if available == False:
        new_data = {'alat': alat, 'harga': harga}
        with open ('dataalat.csv', 'a', newline='') as file :
            write = csv.DictWriter(file, fieldnames=new_data.keys())
            write.writerow(new_data)
            print('\nTambah alat berhasil !')
            print('-'*35)
            file.flush()
            file.close()
            kembali_1()


def kembali_1():
    jika = input('\nTambah alat lagi ? (y/n) :')

    if jika == 'y':
        print(f'\n{'-'*35}')
        tambah_alat()
    elif jika == 'n':
        clear()
        pilih_satuan()
    else:
        kembali_1()

#============================================================================

def lihat_alat():
    data_alat = []
    with open ('dataalat.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_alat.append([row[0],row[1]])

    kolom =['Alat', 'Harga']
    df = pd.DataFrame(data_alat, columns=kolom)
    df.index += 1
    print(df) 
    kembali_satuan()  

def kembali_satuan():
    back = input('\nKembali >> (klik enter)')
    if back == '':
        clear()
        pilih_satuan()
    else:
        kembali_satuan()


#============================================================================

def update_alat():
    print(f'{'Update Alat':^35}\n')

    data_alat = []
    with open ('dataalat.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_alat.append([row[0],row[1]])

    kolom = ['Alat','Harga']
    df = pd.DataFrame(data_alat, columns=kolom)
    df.index += 1
    print(df)

    try:
        baris_input = input('\nNomor baris yang ingin diupdate (enter = cancel) : ')
        if not baris_input:
            print('\nCancel !')
            pilih_satuan()
        baris = int(baris_input)

    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        update_alat()

    data = 0
    for data_perbaris in range(len(data_alat)):
        if data_perbaris + 1 == baris:
            data = 1

    if data == 0:
        print('\nTidak ada data pada baris tersebut !')
        print('-'*35)
        update_alat()

    alat = input('Nama Alat : ')
    if len(alat) < 1 or alat == '':
        print('\nMasukkan nama alat !')
        print('-'*35)
        update_alat() 
        
    harga = input('Harga Sewa per Hari : ')
    if len(harga) < 3 or harga == '':
        print('\nMasukkan harga (dalam rupiah) !')
        print('-'*35)
        update_alat()
    
    for data_perbaris in range(len(data_alat)) :
        if data_perbaris + 1 == baris :
            data_alat[data_perbaris][0] = alat
            data_alat[data_perbaris][1] = harga

    with open ('dataalat.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(data_alat)

    clear()
    print('\nData berhasil di update !')
    pilih_satuan()
   
#============================================================================

def hapus_alat():
    print(f'{'Hapus Alat':^35}\n')

    data_alat = []
    with open('dataalat.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_alat.append([row[0],row[1]])

    kolom = ['Alat','Harga']
    df = pd.DataFrame(data_alat, columns=kolom)
    df.index += 1
    print(df)

    try:
        baris_input = input('\nNomor baris yang ingin diupdate (enter = cancel) : ')
        if not baris_input:
            print('\nCancel !')
            pilih_satuan()
        baris = int(baris_input)

    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        hapus_alat()

    data = 0

    for data_perbaris in range(len(data_alat)):
        if data_perbaris + 1 == baris:
            data = 1
            data_alat.pop(data_perbaris)
            with open ('dataalat.csv', 'w', newline='') as file:
                write = csv.writer(file)
                write.writerows(data_alat)

            clear()
            print('\nData berhasil dihapus !')
            pilih_satuan()

    if data == 0:
        print('\nTidak ada data pada baris tersebut !')
        print('-'*35)
        hapus_alat()


    
#============================================================================

#Paketan

def tambah_paket():
    print(f'{'Tambah Paket ':^35}')

    paket = input('\nNama Paket : ')
    if paket == '':
        print('\nMasukkan nama paket !')
        print('-'*35)
        tambah_paket()

    data_alat = []
    with open('dataalat.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_alat.append({'alat':row[0],'harga':row[1]})

        df = pd.DataFrame(data_alat)
        df.index += 1
        print(f'\n{df}')

    try:
        jumlah_alat_input = input('\nJumlah alat yang ingin dimasukkan : ')
        if not jumlah_alat_input:
            print('\nMasukkan jumlah alat yang ingin dimasukkan !')
            print('-'*35)
            tambah_paket()

        jumlah_alat = int(jumlah_alat_input)
        if jumlah_alat < 2:
            print('\nMinimal 2 alat dalam paket !')
            print('-'*35)
            tambah_paket()
    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        tambah_paket()
        
    list_alat = []
    harga = 0

    data_paket = []
    with open('datapaket.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_paket.append({'namapaket':row[0], 'alat':row[1], 'harga':row[2], 'diskon':row[3]})

    for i in range(jumlah_alat) :
        try:
            no_alat_input = input('Nomor alat : ')
            if not no_alat_input:
                print('\nMasukkan nomor alat !')
                print('-'*35)
                tambah_paket()
            no_alat = int(no_alat_input)
        except ValueError:
            print('\nMasukkan input berupa angka !')
            print('-'*35)
            tambah_paket()
        for j in range(1,len(data_alat)+1) :
              if j == no_alat :
                list_alat.append(data_alat[j-1]['alat'])
                harga += int(data_alat[j-1]['harga'])
    
    diskon_input = input('Masukkan diskon (%) : ')
    try:
        if not diskon_input:
                print('\nMasukkan diskon !')
                print('-'*35)
                tambah_paket()
        diskon = int(diskon_input)
    except ValueError:
            print('\nMasukkan input berupa angka !')
            print('-'*35)
            tambah_paket()
    hitung = int(harga-(harga*diskon/100))

    data_paket = {'namapaket': paket, 'alat': list_alat, 'harga' : harga, 'diskon' : hitung}
    with open ('datapaket.csv', 'a', newline='') as file :
        write = csv.DictWriter(file, fieldnames=data_paket.keys())
        write.writerow(data_paket)

    print('\nTambah paket berhasil !')
    print('='*35)
    kembali_2()

def kembali_2():
    jika = input('\nIngin menambahkan lagi ? (y/n) : ')

    if jika == 'y':
        print(f'\n{'='*35}')
        tambah_paket()
    elif jika == 'n':
        clear()
        pilih_paketan()
    else:
        kembali_2()
        
#============================================================================

def lihat_paket():
    print(f'{'Data Paket ':^35}\n')

    data_paket = []
    with open('datapaket.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_paket.append([row[0],row[1], row[2],row[3]])
    
    kolom = ['Nama Paket', 'Alat', 'Harga', 'Diskon']
    df = pd.DataFrame(data_paket, columns=kolom)
    df.index += 1 
    print(df)
    kembali_paketan()

def kembali_paketan():
    back = input('\nKembali >> (klik enter)')
    if back == '':
        clear()
        pilih_paketan()
    else:
        kembali_paketan()
    
#============================================================================

def update_paket():
    print(f'{'Update Paket ':^35}\n')

    data_paket = []
    with open ('datapaket.csv', 'r') as file:
        read = csv.reader(file)
        for row in read:
            data_paket.append([row[0],row[1], row[2],row[3]])

    kolom = ['Nama Paket', 'Alat', 'Harga', 'Diskon']
    df = pd.DataFrame(data_paket, columns=kolom)
    df.index += 1
    print(df)

    try:
        baris_input = input('\nNomor baris yang ingin diupdate (enter = cancel) : ')
        if not baris_input:
            print('\nCancel !')
            pilih_paketan()
        baris = int(baris_input)
    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        update_paket()

    data = 0
    for data_perbaris in range(len(data_paket)):
        if data_perbaris + 1 == baris:
            data = 1

    if data == 0:
        print('\nTidak ada data pada baris tersebut !')
        print('-'*35)
        update_paket()

    paket = input('\nNama Paket : ')
    if paket == '':
        print('\nMasukkan nama paket !')
        print('-'*35)
        update_paket()

    print('\n')

    data_alat = []
    with open('dataalat.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_alat.append({'alat':row[0],'harga':row[1]})

        df = pd.DataFrame(data_alat)
        df.index += 1
        print(df)

    try:
        jumlah_alat_input = input('\nJumlah alat yang ingin dimasukkan : ')
        if not jumlah_alat_input:
            print('\nMasukkan jumlah alat yang ingin dimasukkan !')
            print('-'*35)
            update_paket()

        jumlah_alat = int(jumlah_alat_input)
        if jumlah_alat < 2:
            print('\nMinimal 2 alat dalam paket !')
            print('-'*35)
            update_paket()
    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        update_paket()

    list_baru = []
    harga = 0

    data_alat = []
    with open ('dataalat.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_alat.append({'alat':row[0],'harga':row[1]})

    for i in range(jumlah_alat) :
        try:
            no_alat_input = input('Nomor alat : ')
            if not no_alat_input:
                print('\nMasukkan nomor alat !')
                print('-'*35)
                update_paket()
            no_alat = int(no_alat_input)
        except ValueError:
            print('\nMasukkan input berupa angka !')
            print('-'*35)
            update_paket()
        for j in range(1,len(data_alat)+1) :
              if j == no_alat :
                list_baru.append(data_alat[j-1]['alat'])
                harga += int(data_alat[j-1]['harga'])

    diskon_input = input('Masukkan diskon (%) : ')
    try:
        if not diskon_input:
                print('\nMasukkan diskon !')
                print('-'*35)
                update_paket()
        diskon = int(diskon_input)

    except ValueError:
            print('\nMasukkan input berupa angka !')
            print('-'*35)
            update_paket()

    hitung = int(harga-(harga*diskon/100))

    for data_perbaris in range(len(data_paket)):
        if data_perbaris + 1 == baris:
            data_paket[data_perbaris][0] = paket
            data_paket[data_perbaris][1] = list_baru
            data_paket[data_perbaris][2] = harga
            data_paket[data_perbaris][3] = hitung

    with open ('datapaket.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(data_paket)

    clear()
    print('\nData paket berhasil di update !')
    pilih_paketan()

#============================================================================

def hapus_paket():
    print(f'{'Hapus Paket':^35}\n')

    data_paket = []
    with open('datapaket.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_paket.append([row[0],row[1],row[2],row[3]])

    kolom = ['Nama Paket', 'Alat', 'Harga', 'Diskon']
    df = pd.DataFrame(data_paket, columns=kolom)
    df.index += 1
    print(df)

    try:
        baris_input = input('\nNomor baris yang ingin dihapus (enter = cancel) : ')
        if not baris_input:
            print('\nCancel !')
            pilih_satuan()
        baris = int(baris_input)   

    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        hapus_paket()

    data = 0
    for data_perbaris in range(len(data_paket)):
        if data_perbaris + 1 == baris:
            data = 1
            data_paket.pop(data_perbaris)

    if data == 0:
        print('\nTidak ada data pada baris tersebut !')
        print('-'*35)
        hapus_paket() 

    with open ('datapaket.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(data_paket)    

    clear()
    print('\nData paket berhasil dihapus !')
    pilih_paketan()
#============================================================================
#function, Menu 1. Kelola Alat Camping
#============================================================================

#============================================================================
#Function, Menu 2. Pesanan Customer 
#============================================================================

def menu_dua_admin():
    print(f'{'='*37}')
    print(f'|{'List Pesanan':^35}|')
    print(f'{'='*37}\n')

    data_pesanan = []
    with open ('datapesanan.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_pesanan.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
    
    kolom = ['username','nama','no.telp','listalat/paket','totalharga','tipe','status']
    df = pd.DataFrame(data_pesanan, columns=kolom)
    df.index += 1
    print(df)

    menu = input('\n[1] Terima pesanan \n[2] Hapus pesanan \n[3] Kembali \n\nPilih menu : ')

    if menu == '1':
        print('-'*35)
        terima_pesanan()

    elif menu == '2':
        print('-'*35)
        hapus_pesanan()

    elif menu == '3':
        clear()
        home_admin()
    
    else:
        clear()
        print('Masukkan nomor menu yang sesuai !')
        menu_dua_admin()

#============================================================================

def terima_pesanan():
    data_pesanan = []
    with open ('datapesanan.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_pesanan.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
    
    kolom = ['username','nama','no.telp','listalat/paket','totalharga','tipe','status']
    df = pd.DataFrame(data_pesanan, columns=kolom)
    df.index += 1
    print(df)

    status = 'accept'

    try:
        baris_input = input('Nomor baris yang ingin di accept (enter = cancel) : ')
        if not baris_input:
            print('\nCancel !')
            menu_dua_admin()
        baris = int(baris_input)
    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        terima_pesanan()

    data = 0
    for data_perbaris in range(len(data_pesanan)):
        if data_perbaris + 1 == baris:
            data_pesanan[data_perbaris][6] = status
            data = 1

            with open ('datapesanan.csv', 'w', newline='') as file:
                write = csv.writer(file)
                write.writerows(data_pesanan)

    if data == 0:
        print('\nTidak terdapat data pesanan pada nomor tersebut !')
        print('-'*35)
        terima_pesanan()

    clear()
    print('\nPesanan berhasil diaccept !')
    menu_dua_admin()

#============================================================================

def hapus_pesanan():
    data_pesanan = []
    with open ('datapesanan.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_pesanan.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
    
    kolom = ['username','nama','no.telp','listalat/paket','totalharga','tipe','status']
    df = pd.DataFrame(data_pesanan, columns=kolom)
    df.index += 1
    print(df)

    try:
        baris_input = input('Nomor baris yang ingin di hapus (enter = cancel) : ')
        if not baris_input:
            print('\nCancel !')
            menu_dua_admin()
        baris = int(baris_input)
    except ValueError:
        print('\nMasukkan input berupa angka !')
        print('-'*35)
        hapus_pesanan()

    data = 0
    for data_perbaris in range(len(data_pesanan)):
        if data_perbaris + 1 == baris:
            data_pesanan.pop(data_perbaris)
            data = 1
            with open ('datapesanan.csv', 'w', newline='') as file:
                write = csv.writer(file)
                write.writerows(data_pesanan) 

    if data == 0:
        print('\nTidak terdapat data pesanan pada nomor tersebut !')
        print('-'*35)
        hapus_pesanan()

    clear()
    print('\nPesanan berhasil di hapus !')
    menu_dua_admin()
        
#============================================================================
#Akhir Function, Menu 2. Pesanan Customer
#============================================================================

#============================================================================
#Akhir Sebagai Admin
#============================================================================

#============================================================================
#Sebagai Customer
#============================================================================

def home_customer():
    print(f'Selamat Datang, {data_login[0]['nama']} !') 
        
    print('\n[1] Pesan \n[2] Lihat pesanan \n[3] Log out')
    pilih_menu = input('\nPilih menu : ')
     
    if pilih_menu == '1':
        clear()
        tambah_pesanan_customer()

    elif pilih_menu == '2':
        clear()
        lihat_pesanan_customer()

    elif pilih_menu == '3':
        clear()
        sign()

    else:
        print('\nMasukkan nomor menu yang sesuai !')
        print('-'*35)
        home_customer()

#============================================================================
#Function, menu 1. Tambah pesanan
#============================================================================

def tambah_pesanan_customer():
    print('='*37)
    print(f'|{'Pesan':^35}|')
    print('='*37)
    print('\n[1] Satuan \n[2] Paketan \n[3] Kembali')
    pilih = input('\nPilih menu : ')

    if pilih == '1':
        clear()
        pesanan_satuan_customer()

    elif pilih == '2':
        clear()
        pesanan_paketan_customer()

    elif pilih == '3':
        clear()
        home_customer()

    else:
        print('\nMasukkan nomor menu yang sesuai !')
        tambah_pesanan_customer()
        

#============================================================================
pesan_satuan = []

def pesanan_satuan_customer():
    print('='*37)
    print(f'|{'Pesan Satuan':^35}|')
    print(f'{'='*37}\n')

    pesan_satuan.clear()

    with open ('dataalat.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            pesan_satuan.append([row[0],row[1]]) 
        
    kolom = ['Alat', 'Harga']
    df = pd.DataFrame(pesan_satuan, columns=kolom)
    df.index += 1
    print(df)

    try:
        jumlah_alat_input = input('\nJumlah alat yang ingin dipesan (enter = cancel) : ')
        if not jumlah_alat_input:
            print('\nCancel !')
            tambah_pesanan_customer()
        jumlah_alat = int(jumlah_alat_input)
        
    except ValueError:
        clear()
        print('\nMasukkan input berupa angka !')
        pesanan_satuan_customer()
        
    list_alat = []
    harga = 0
    tipe = 'satuan'
    status = 'waiting'
    username = data_login[0]['username']
    nama_customer = data_login[0]['nama']
    telpon_customer = data_login[0]['no.telp']

    for i in range(jumlah_alat) :
        try:
            no_alat_input = input('Nomor alat : ')
            if not no_alat_input:
                print('\nMasukkan nomor alat !')
                print('-'*35)
                pesanan_satuan_customer()
            no_alat = int(no_alat_input)
        except ValueError:
            print('\nMasukkan input berupa angka !')
            print('-'*35)
            pesanan_satuan_customer()
        for j in range(1,len(pesan_satuan)+1) :
              if j == no_alat :
                list_alat.append(pesan_satuan[j-1][0])
                harga += int(pesan_satuan[j-1][1])

    data_paket = {'username':username,'nama':nama_customer,
                  'no.telp':telpon_customer,'alat': list_alat, 
                  'harga' : harga,'tipe': tipe, 'status': status}
    with open ('datapesanan.csv', 'a', newline='') as file :
        write = csv.DictWriter(file, fieldnames=data_paket.keys())
        write.writerow(data_paket)

    print('\nPesanan berhasil ditambahkan !')
    print('-'*35)
    jika = input('\nIngin menambahkan lagi ? (y/n) : ')

    if jika == 'y':
        clear()
        pesanan_satuan_customer()
    else:
        clear()
        print('\nPesanan berhasil ditambahkan !')
        tambah_pesanan_customer()

#============================================================================
pesan_paketan = []

def pesanan_paketan_customer():
    print('='*37)
    print(f'|{'Pesan Paketan':^35}|')
    print(f'{'='*37}\n')

    pesan_paketan.clear()

    with open ('datapaket.csv','r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            pesan_paketan.append([row[0], row[1], row[2], row[3]]) 

    kolom = ['Nama Paket','Alat','Harga','Diskon']
    df = pd.DataFrame(pesan_paketan, columns=kolom)
    df.index += 1
    print(df)

    list_alat = []
    harga = 0
    tipe = 'paket'
    status = 'waiting'
    username = data_login[0]['username']
    nama_customer = data_login[0]['nama']
    telpon_customer = data_login[0]['no.telp']

    try:
        no_paket_input = input('\nNomor paket yang ingin dipesan (enter = cancel) : ')
        if not no_paket_input:
            print('\nCancel !')
            tambah_pesanan_customer()
        no_paket = int(no_paket_input)
    
    except ValueError:
        clear()
        print('\nMasukkan input berupa angka !')
        pesanan_paketan_customer()

    for i in range(1,len(pesan_paketan)+1) :
        if i == no_paket :
            list_alat.append(pesan_paketan[i-1][0])
            harga += int(pesan_paketan[i-1][2])

    data_paket = {'username':username,'nama':nama_customer,
                  'no.telp':telpon_customer,'alat': list_alat, 
                  'harga' : harga,'tipe':tipe, 'status': status}
    with open ('datapesanan.csv', 'a', newline='') as file :
        write = csv.DictWriter(file, fieldnames=data_paket.keys())
        write.writerow(data_paket)

    clear()
    print('\nPesanan berhasil ditambahkan !')
    tambah_pesanan_customer()
   

#============================================================================

def lihat_pesanan_customer():
    clear()
    print(f'{'Pesanan Anda':^35}\n')
    data_pesanan = []
    data_customer = []

    with open ('datapesanan.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        for row in read:
            data_pesanan.append({'username':row[0],'nama':row[1], 
                                 'no.telp':row[2], 'listalat/paket':row[3], 
                                 'totalharga':row[4], 'tipe':row[5], 
                                 'status':row[6]})

    for i in data_pesanan :
        if i['username'] == data_login[0]['username'] :
            data_customer.append(i)
    
    df = pd.DataFrame(data_customer)
    df.index += 1
    print(df)
    kembali_3()

def kembali_3():
    back = input('\nKembali >> (enter)')

    if back == '':
        print('='*35)
        home_customer()
    else:
        kembali_3()

    

#============================================================================
#Akhir function, menu 1. Tambah pesanan
#============================================================================


#============================================================================
#Akhir Sebagai Customer
#============================================================================


#============================================================================
#RUNNING PROGRAM
#============================================================================
sign()



