# Cashier - Project

## Latarbelakang Problems
Program Super Cashier adalah program yang memiliki fungsi utama untuk membantu pemilik-pemilik usaha untuk bisa melakukan transaksi lebih cepat dan efisien dibandingkan dengan transaksi konvensional. Selain itu, Program Super Cashier akan membantu sebuah perusahaan untuk mencatat transaksi menjadi lebih akurat dan cepat
## Alur Program
Program ini memiliki alur sebagai berikut:
1. User akan membuat ID transaksi customer. ID transaksi dapat berupa string apapun, seperti "trnsct_123". ID transaksi dapat dibuat seperti ini "trnsct123 = Transaction()"

2. User akan memasukkan item dengan method "add_item" dengan informasi nama, jumlah, harga per item sebagai parameter (trnsct_123.add_item(nama item, jumlah item, harga per item))

3. User dapat melakukan perubahan pada pesanan (nama item, jumlah item, dan harga per item). Jika ingin mengubah nama item, dapat diubah dengan method update_item_name(nama item, update nama item). Jika ingin mengubah jumlah item, dapat diubah dengan method update_item_qty(nama item, update jumlah item). Jika ingin mengubah harga item, dapat diubah dengan method update_item_price(nama item, update harga item)

4. Untuk penghapusan item, terdapat beberapa opsi: penghapusan salah satu item, penghapusan keseluruhan pesanan. Jika ingin menghapus salah satu item, item dapat dihapus dengan menggunakan method delete_item(nama item). Jika ingin menghapus keseluruhan item, dapat menggunakan method reset_transaction()

5. User akan mengecek pesanan dengan method check_order. Program akan mengecek apakah terdapat kesalahan input pada pesanan, seperti jumlah item dan harga dengan value 0, dan string kosong pada nama item. Jika terdapat kesalahan input, program mengeluarkan output error. Jika tidak terdapat kesalahan input, program akan mengeluarkan output berupa transaksi dari item-item yang sudah dibeli.

6. User akan mengecek total harga pada transaksi dengan menggunakan method total_price. Program akan menghitung subtotal dari pesanan dengan menghitung keseluruhan harga pada setiap item, lalu menghitung total harga dengan mengecek kondisi diskon dari subtotal.

## Penjelasan Kode
## Hasil Test Case
## Conclusion
