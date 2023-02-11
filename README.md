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
Pilihan opsi dan Opsi 1 #1 <br />
![image](https://user-images.githubusercontent.com/113890684/218240907-685763f1-568f-457e-9d1b-46478fe0734b.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218240925-2a91f532-1dd4-49e2-9c16-c068fcd9c81d.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218240939-97e4fdd1-69f8-4f51-9b1b-1df8863b4024.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218240951-d6da0d7e-5bcb-434e-8e8b-532062733881.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218240977-e415262f-7b7e-441d-9a12-24af68b63a29.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241019-4a16bf65-b26d-4619-b375-74d566170194.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241042-f33defb4-80db-41d3-9995-b3a4c71baad6.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241058-9d1ede13-3044-445a-b3cf-c76e45d1fc42.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241082-34da4ceb-c141-470a-aac8-8287a4d034c0.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241098-11bbb46e-b8ef-4ad5-9a18-b298b82ee27e.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241128-5121cbc3-5716-4b3e-8af3-39bf943036ee.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241152-f335dd21-8f9d-4ce2-98b6-9e41e09c91b8.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241198-13484e49-68ae-42f5-97c5-4f793950ebbd.png)<br />
![image](https://user-images.githubusercontent.com/113890684/218241321-115c4da5-5530-4385-8c81-23d2084cf66c.png)<br />

## Conclusion
