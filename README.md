# Super Cashier

## Latar Belakang
Super Cashier adalah sistem kasir self-service untuk sebuah supermarket. Pelanggan bisa langsung memasukkan item, jumlah item, dan harga item yang dibeli.
Modul dibuat dengan menerapkan Object Oriented Programming, function, try-except, documentation, dan clean code.

## Objektif
Alur belanja:
1. Customer membuat ID transaksi customer
2. Customer memasukkan nama item, jumlah item, dan harga item yang dibeli
3. Jika ternyata ada kesalahan dalam memasukkan nama item, jumlah item, atau harga item, customer bisa melakukan update item:
   a. update nama item
   b. update jumlah item
   c. update harga item
4. Jika batal membeli suatu item, customer bisa melakukan hapus item:
   a. hapus 1 item
   b. reset seluruh transaksi
5. Jika sudah selesai berbelanja, tetapi masih ragu apakah harga barang dan nama yang diinput sudah benar, customer bisa melakukan check order dengan output sebagai berikut:
   a. Mengeluarkan pesan "Pemesanan sudah benar" jika tidak ada kesalahan input.
   b. Mengeluarkan pesan "Terdapat kesalahan input data" jika terjadi kesalahan input.
   c. Menampilkan tabel berisi seluruh data pesanan.
6. Terakhir, customer bisa menampilkan total belanja yang harus dibayar dan diskon yang didapatkan (jika ada).

## Alur Code / Flowchart
```mermaid
flowchart TD;
    A([start])-->B[membuat ID transaksi dengan class Transaction];
    B-->C[memasukkan item dengan fungsi add_item];
    C-->D{ada data yang ingin diubah?};
    D--Ya-->E[update nama/jumlah/harga dengan fungsi update_item];
    D--Tidak-->F{ada item yang ingin dibatalkan?};
    E-->F;
    F--Ya-->G[hapus item dengan fungsi delete_item atau reset_transaction];
    G-->H{masih ada item yang ingin ditambahkan?};
    F--Tidak-->H;
    H--Ya-->C;
    H--Tidak-->I[mengecek dan menampilkan pesanan dengan fungsi check_order];
    I-->J{input sudah benar?};
    J--Ya-->K[menghitung total belanja dengan fungsi total_price];
    J--Tidak-->E;
    K-->L{total belanja>500.000?};
    L--Ya-->M[diskon 10%];
    M-->N{total belanja>300.000?};
    L--Tidak-->N;
    N--Ya-->O[diskon 8%];
    O-->P{total belanja>200.000?};
    N--Tidak-->P;
    P--Ya-->Q[diskon 5%];
    Q-->R[menampilkan total belanja setelah diskon];
    P--Tidak-->R;
    R-->S([selesai]);
```

## Penjelasan dari Function

## Demonstrasi

## Kesimpulan
Contoh tampilan daftar belanja dan total yang harus dibayar:

| Nama Item   |   Jumlah Item |   Harga/Item |   Total Harga |
|-------------|---------------|--------------|---------------|
| Chitato     |            10 |         6000 |         60000 |
| Roti Tawar  |            10 |        11000 |        110000 |
| Teh Botol   |            10 |         3500 |         35000 |

Pemesanan sudah benar.

Anda mendapatkan diskon 5% sebesar Rp 10250. Total belanja Anda adalah Rp 194750 (sudah termasuk diskon).
