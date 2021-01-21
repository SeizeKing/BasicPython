#!/usr/bin/env python
# coding: utf-8

# In[82]:


auth = True
contacts = {}
contactlist = []

def menu():
    print("\n\nSelamat Datang!\n")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar\n")

def form_tambah_kontak():
    nama = input("Masukkan Nama : ")
    nohp = input("Masukkan No Telepon : ")
    contacts[nama] = nohp
    print("Kontak berhasil ditambahkan!!")
    
menu()
choose = int(input("Pilih Menu : "))

while auth:
    if choose == 1:
        print("\nDAFTAR KONTAK\n")
        if not contacts:
            print("Belum ada data!!")
            menu()
            choose = int(input("Pilih Menu : "))
        else:
            for key, value in contacts.items():
                print("Nama : " + key + "\nUmur : " + value)
            menu()
            choose = int(input("Pilih Menu : "))
    
    elif choose == 2:
        form_tambah_kontak()
        menu()
        choose = int(input("Pilih Menu : "))
    elif choose == 3:
        print("Program Selesai, Sampai Jumpa Lagi")
        auth = False
    else:
        print("\nMenu Tidak Ditemukan")
        menu()
        choose = int(input("Pilih Menu : "))
    


# In[ ]:




