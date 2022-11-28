import pandas as pd
from tabulate import tabulate

class Transaction:
    def __init__(self):
        '''Fungsi inisialisasi untuk class Transaction
        dict_txn (dict) = dictionary untuk menyimpan data transaksi (dict)
        txn_valid (boolean) = untuk menandai apakah data yang diinput ke dalam dictionary transaksi sudah valid.
                            Nilai awal adalah True dan bisa berubah False setelah dicek validitasnya lewat fungsi.'''
        
        self.dict_txn = dict()
        self.txn_valid = True
    
    def add_item(self, nama, jumlah, harga):
        '''Fungsi untuk menambahkan item ke dalam dictionary transaksi.
        nama (String, key) = nama item yang dibeli, key dalam dictionary
        jumlah (int) = jumlah item yang dibeli
        harga (int) = harga per item'''
        
        #mengecek tipe data integer
        if type(jumlah)!=int:
            print("Jumlah barang harus berupa angka!")
        
        elif type(harga)!=int:
            print("Harga barang harus berupa angka!")
        
        else:
            #memasukkan data ke dalam dictionary
            dict_add = {nama: [jumlah, harga, jumlah*harga]}
            self.dict_txn.update(dict_add)
            print(f"Menambahkan ke dalam pesanan: {nama} sejumlah {jumlah} dengan harga Rp {harga}.")
    
    
    def update_item_name(self, nama, nama_baru):
        '''Fungsi untuk mengubah nama item dalam dictionary yang sudah diinput.
        nama (String) = nama item sebelum diganti, key dari dictionary
        nama_baru (String) = nama baru untuk item, menjadi key baru dari dictionary'''
            
        temp = self.dict_txn[nama]
        self.dict_txn.pop(nama)
        self.dict_txn.update({nama_baru: temp})
        
        #menampilkan data pesanan setelah terjadi perubahan
        self.print_order()
        print(f"Mengubah nama item {nama} menjadi {nama_baru}.")
    
    
    def update_item_qty(self, nama, jumlah_baru):
        '''Fungsi untuk mengubah jumlah item dalam dictionary yang sudah diinput.
        nama (String) = nama item yang ingin diubah jumlahnya, key dari dictionary
        jumlah_baru (int) = jumlah baru dari nama item yang dibeli'''
            
        #mengecek tipe data integer
        if type(jumlah_baru)!=int:
            print("Jumlah barang harus berupa angka!")
        
        else:
            #memasukkan data ke dalam dictionary
            self.dict_txn[nama][0] = jumlah_baru
            self.dict_txn[nama][2] = jumlah_baru*self.dict_txn[nama][1]
        
            #menampilkan data pesanan setelah terjadi perubahan
            self.print_order()
            print(f"Mengubah jumlah item {nama} menjadi {jumlah_baru}.")
    
    
    def update_item_price(self, nama, harga_baru):
        '''Fungsi untuk mengubah harga item dalam dictionary yang sudah diinput.
        nama (String) = nama item yang ingin diubah jumlahnya, key dari dictionary
        harga_baru (int) = harga baru dari nama item yang dibeli'''

        #mengecek tipe data integer        
        if type(harga_baru)!=int:
            print("Harga barang harus berupa angka!")
        
        else:
            #memasukkan data ke dalam dictionary
            self.dict_txn[nama][1] = harga_baru
            self.dict_txn[nama][2] = harga_baru*self.dict_txn[nama][0]
            
            #menampilkan data pesanan setelah terjadi perubahan
            self.print_order()
            print(f"Mengubah harga item {nama} menjadi {harga_baru}.")
    
    
    def delete_item(self, nama):
        '''Fungsi untuk menghapus data nama item beserta jumlah dan harganya dari dictionary.
        nama (String) = nama item yang ingin dihapus'''
        
        try:
            self.dict_txn.pop(nama)
            print(f"Menghapus pesanan {nama}.")
            self.print_order()
        
        except KeyError:
            print(f"{nama} tidak ada dalam daftar pesanan.")
        
    
    def reset_transaction(self):
        '''Fungsi untuk menghapus semua data pesanan dalam dictionary.'''
        
        self.dict_txn = self.dict_txn.clear
        print("Semua item berhasil dihapus.")
    

    def print_order(self):
        '''Fungsi untuk menampilkan semua pesanan dalam dictionary.'''
        
        try:
            table_txn = pd.DataFrame(self.dict_txn).T
            headers = ["Nama Barang", "Jumlah", "Harga", "Total"]
            print(tabulate(table_txn, headers, tablefmt="github"))
        
        except:
            print("Belum ada pemesanan.")
            
            
    def check_order(self):
        '''Fungsi untuk mengecek validitas dan menampilkan semua pesanan dalam dictionary.'''
        
        try:
            #menampilkan semua pesanan
            table_txn = pd.DataFrame(self.dict_txn).T
            headers = ["Nama Barang", "Jumlah", "Harga", "Total"]
            print(tabulate(table_txn, headers, tablefmt="github"))

            #mengecek jumlah/harga lebih dari 0
            kolom=0
            while kolom<2:
                for data in table_txn[kolom]:
                    if data<=0:
                        self.txn_valid = False
                kolom+=1

            if self.txn_valid:
                print("Pemesanan sudah benar.")
            else:
                print("Terdapat kesalahan input jumlah/harga. Mohon cek ulang pesanan.")
        
        except ValueError:
            print("Belum ada pemesanan.")

            
    def total_price(self):
        '''Fungsi untuk menampilkan semua pesanan dan total belanja.'''
        
        #memastikan pesanan sudah valid sebelum menjalankan method
        self.check_order()
        
        #menghitung diskon yang didapat
        if self.txn_valid:
            total_belanja = 0

            for item in self.dict_txn:
                total_belanja += self.dict_txn[item][2] 

            if total_belanja>500_000:
                diskon = int(total_belanja*0.1)
                total_belanja = int(total_belanja-diskon)
                print(f"Anda mendapatkan diskon 10% sebesar Rp {diskon}. Total belanja Anda adalah Rp {total_belanja} (sudah termasuk diskon).")        

            elif total_belanja>300_000:
                diskon = int(total_belanja*0.08)
                total_belanja = int(total_belanja-diskon)
                print(f"Anda mendapatkan diskon 8% sebesar Rp {diskon}. Total belanja Anda adalah Rp {total_belanja} (sudah termasuk diskon).")

            elif total_belanja>200_000:
                diskon = int(total_belanja*0.05)
                total_belanja = int(total_belanja-diskon)
                print(f"Anda mendapatkan diskon 5% sebesar Rp {diskon}. Total belanja Anda adalah Rp {total_belanja} (sudah termasuk diskon).")

            else:
                print(f"Total belanja Anda adalah Rp {total_belanja}.")
        
        else:
            print("Total belanja belum bisa dihitung selama masih ada kesalahan input.")