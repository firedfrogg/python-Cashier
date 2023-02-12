from cashier import *
trnsct = Transaction()
conditions = True

print("-------------------")
print("SELAMAT DATANG DI PROGRAM SUPER CASHIER")
print("-------------------")

while conditions:
    print("1. Tambah Item\n2. Ubah Nama Item\n3. Ubah Jumlah Item\n4. Ubah Harga Item\n5. Hapus Item\n"
          "6. Hapus semua Item\n7. Cek Pesanan\n8. Exit\n")
    opsi = int(input("Silakan masukkan opsi: "))
    if opsi == 1:
        try:
            nama_item = input("Masukkan nama item: ")
            jumlah_item = int(input("Masukkan jumlah item: "))
            harga_item = int(input("Masukkan harga item: "))
            trnsct.add_item(nama_item, jumlah_item, harga_item)
        except ValueError:
            print("Jumlah dan harga dari item harus berupa angka!\n")
    elif opsi == 2:
        nama_lama = input("Masukkan nama item yang ingin diubah: ")
        nama_baru = input("Masukkan nama item yang baru: ")
        trnsct.update_item_name(nama_lama, nama_baru)
    elif opsi == 3:
        try:
            cek_nama = input("Masukkan nama item yang jumlahnya ingin diubah: ")
            jumlah_baru = int(input("Masukkan jumlah item yang baru: "))
            trnsct.update_item_qty(cek_nama, jumlah_baru)
        except ValueError:
            print("Jumlah item harus berupa angka!\n")
    elif opsi == 4:
        try:
            cek_nama = input("Masukkan nama item yang harganya ingin diubah: ")
            harga_baru = int(input("Masukkan harga item yang baru: "))
            trnsct.update_item_price(cek_nama, harga_baru)
        except ValueError:
            print("Harga item harus berupa angka!\n")
    elif opsi == 5:
        cek_nama = input("Masukkan nama item yang ingin dihapus: ")
        trnsct.delete_item(cek_nama)
    elif opsi == 6:
        reset_pesanan = True
        while reset_pesanan:
            opsi = input("Apakah anda yakin ingin menghapus keseluruhan pesanan? Y/N ").lower()
            if opsi == "y":
                trnsct.reset_transaction()
                break
            elif opsi == "n":
                break
            else:
                print("Input tidak valid!")
    elif opsi == 7:
        trnsct.check_order()
    elif opsi == 8:
        print("Behasil keluar dari program!")
        exit()
    else:
        print("Input Tidak Valid!\n")