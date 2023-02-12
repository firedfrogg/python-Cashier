class Transaction:
    def __init__(self):
        self.pesanan = {}
        self.keys = []
        self.values = []
        self.total_harga = 0

    def add_item(self, nama, jumlah, harga):
        """ Fungsi ini akan menambah item-item di parameter ke dalam dictionary self.pesanan"""
        try:
            self.pesanan[nama] = [jumlah, harga, jumlah*harga]
            print(f"Item {nama} berhasil ditambahkan!\n")
        except ValueError:
            print("Harga dan jumlah item harus berupa angka!\n")

    def update_item_name(self, nama, nama_baru):
        """
            Fungsi ini akan membuat duplikasi item di paramter 'nama' dengan paramter 'nama_baru'
            lalu menghapus key dan value dengan parameter 'nama' di dictionary self.pesanan
        """
        if nama in self.pesanan:
            self.pesanan[nama_baru] = self.pesanan[nama]
            del self.pesanan[nama]
            print(f"Item {nama} berhasil diubah menjadi {nama_baru}!\n")
        else:
            print(f"Item {nama} tidak ditemukan\n")

    def update_item_qty(self, nama, jumlah_baru):
        """
            Fungsi ini akan mengakses dictionary key parameter 'nama' dan mengubah value di indeks 0 (jumlah item)
            dengan value yang terdapat di parameter 'jumlah baru' serta mengubah value di indeks 2 dengan perkalian
            dari 'jumlah_baru' dan indeks 1 (harga satu item)
        """
        try:
            if nama in self.pesanan:
                self.pesanan[nama][0] = jumlah_baru
                self.pesanan[nama][2] = jumlah_baru * self.pesanan[nama][1]
                print(f"Jumlah item {nama} berhasil diubah menjadi {jumlah_baru}!\n")
            else:
                print(f"Item {nama} tidak ditemukan!\n")
        except ValueError:
            print("Jumlah item harus berupa angka!")

    def update_item_price(self, nama, harga_baru):
        """
            Fungsi ini akan mengakses dictionary key parameter 'nama' dan mengubah value di indeks 1 (harga satu item)
            dengan value yang terdapat di parameter 'harga baru' serta mengubah value di indeks 2 dengan perkalian
            dari 'harga_baru' dan indeks 0 (jumlah item)
        """
        try:
            if nama in self.pesanan:
                self.pesanan[nama][1] = harga_baru
                self.pesanan[nama][2] = harga_baru * self.pesanan[nama][0]
                print(f"Harga item {nama} berhasil diubah menjadi {harga_baru}!\n")
            else:
                print(f"Item {nama} tidak ditemukan!\n")
        except ValueError:
            print("Harga item harus berupa angka!")

    def delete_item(self, nama):
        """
            Fungsi ini akan menghapus item di pesanan dengan mengecek parameter 'nama' di key dari
            dictionary self.pesanan. Jika ditemukan, key dari dictionary tersebut akan dihapus beserta
            dengan value di dalamnya. Jika tidak ditemukan, akan mengeluarkan output yang memberi tahu
            bahwa pesanan tersebut tidak ditemukan di dalam dictionary pesanan
        """
        if nama in self.pesanan.keys():
            del self.pesanan[nama]
            print(f"Item {nama} berhasil dihapus!\n")
        else:
            print(f"Item {nama} tidak ditemukan!\n")

    def reset_transaction(self):
        if len(self.pesanan) == 0:
            print("Kamu belum memesan apapun!\n")
        else:
            self.pesanan.clear()
            self.keys.clear()
            self.values.clear()
            print("Pesanan berhasil di-reset!\n")

    def check_order(self):
        """
            Fungsi ini akan mengecek error-error yang terdapat di dictionary pesanan terlebih dahulu
            (0 di dalam value, string kosong di dalam key). Jika tidak teradpat errror pada pesanan tersebut,
            fungsi akan menampilkan output transaksi dari item-item yang sudah dibeli. Jika terdapat error,
            fungsi akan mengeluarkan output berupa error.
        """
        salah_input = False
        for kosong in self.pesanan.values():
            if 0 in kosong:
                salah_input = True

        if salah_input or "" in self.pesanan.keys():
            print("Terdapat kesalahan input data\n")
        elif len(self.pesanan) == 0:
            print("Kamu belum memesan apapun!\n")
        else:
            print("Pemesanan sudah benar")
            for key, values in self.pesanan.items():
                self.keys.append(key)
                self.values.append(values)
            string = "-" * 66
            print('| No | Nama Item      | Jumlah Item     | Harga/Item | Total Harga |')
            print(f"|{string}|")
            for items in range(len(self.keys)):  # For loop untuk menampilkan item-item
                print(f"| {items+1}  | {self.keys[items]:15s}| {self.values[items][0]:<16}| {self.values[items][1]:<11}|"
                      f" {self.values[items][2]:<12}|")
            self.total_price()

    def total_price(self):
        """
            Fungsi ini akan mengeluarkan output berupa subtotal dari pesanan dengan menambah jumlah dari
            variabel total_harga. Lalu, program akan mengecek subtotal untuk pemberikan diskon sesuai dengan
            ketentuan Final Project
        """
        if len(self.pesanan) == 0:
            print("Kamu belum memesan apapun!\n")
        else:
            for harga in range(len(self.values)):
                self.total_harga += self.values[harga][2]
            print(f"Subtotal =  Rp{self.total_harga}")
            if self.total_harga < 200000:
                self.total_harga = self.total_harga
                print(f"Total    =  Rp{self.total_harga}\n")
            elif 200001 <= self.total_harga < 300001:
                self.total_harga = self.total_harga * 0.95
                print(f"Total Setelah Diskon 5% = Rp{self.total_harga}\n")
            elif 300001 <= self.total_harga < 500001:
                self.total_harga = self.total_harga * 0.92
                print(f"Total Setelah Diskon 8% = Rp{self.total_harga}\n")
            else:
                self.total_harga = self.total_harga * 0.90
                print(f"Total Setelah Diskon 10% = Rp{self.total_harga}\n")


