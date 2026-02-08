# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File.txt)

# Nama : Gabriella Anggi Apriliana Tambun
# NIM  :J0403251072
# Kelas:B1
# ==========================================================

# ------------------------------
# Konstanta nama file
# ------------------------------

NAMA_FILE = "stok_barang.txt"

# ----------------------------------------
# Fungsi: Membaca data dari file
# ----------------------------------------
def baca_stok(nama_file):
    #membuat dict kosong untuk tempat data
    stok_dict = {}

    #buka file dan baca seluruh baris
    try:
        with open(nama_file, "r", encoding="utf-8") as file: #membuka file dengan mode baca "r"
            for baris in file: #melakukan perulangan untuk setiap baris dalam file
                baris = baris.strip() #menghapus spasi atau enter diawal dan akhir baris
                if not baris: #jika baris kosong maka lewati
                    continue
                
                parts = baris.split(",") #memecah teks beerdasarkan koma
                if len(parts) == 3:
                    kode, nama, stok = parts
                    #simpan ke dictionary
                    stok_dict[kode] = {
                        "nama": nama, 
                        "stok": int(stok)
                    }
    except FileNotFoundError:
        #jika file belum ada, buat file kosong
        with open(nama_file, "w", encoding="utf-8") as file:
            pass

    return stok_dict #mengembalikan data dict yang sudah terisi ke program

# ----------------------------------------
# Fungsi: Menyimpan data ke file
# ----------------------------------------
def simpan_stok(nama_file, stok_dict):
    
    #tulis ulang seluruh isi file stok_dict
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"] #mengambil jumlah stok dari dictionary berdasarkan kode
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# ----------------------------------------
# Fungsi: Menampilkan semua data
# ----------------------------------------
def tampilkan_semua(stok_dict):
    
    #kalau kosong, menampilkan pesan stok kosong
    if not stok_dict:
        print("Stok kosong.")
        return

    #tampilkan dengan format
    print(f"{'Kode':<10} | {'Nama Barang':<20} | {'Stok':>5}")
    print("-" * 40)
    
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<20} | {stok:>5}")

# ----------------------------------------
# Fungsi: Cari barang berdasarkan kode
# ----------------------------------------
def cari_barang(stok_dict):

    kode = input("Masukkan kode barang: ").strip()

    #cek apakah kode ada di dictionary
    if kode in stok_dict:
        #jika ada: tampilkan detail
        print(f"\nBarang ditemukan:")
        print(f"Kode: {kode}")
        print(f"Nama: {stok_dict[kode]['nama']}")
        print(f"Stok: {stok_dict[kode]['stok']}")
    else:
        #jika tidak ada
        print("Barang tidak ditemukan.")

# ----------------------------------------
# Fungsi: Tambah barang baru
# ----------------------------------------
def tambah_barang(stok_dict):
   
    kode = input("Masukkan kode barang baru: ").strip()
    
    #kode tidak boleh duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip()

    #input stok awal
    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka.")
        return

    #simpan ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }
    
    #simpan ke file agar data aman
    simpan_stok(NAMA_FILE, stok_dict)
    print("Barang berhasil ditambahkan.")

# ----------------------------------------
# Fungsi: Update stok barang
# ----------------------------------------
def update_stok(stok_dict):
    
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    #cek apakah kode ada di dictionary
    if kode not in stok_dict:
        print("Kode tidak ditemukan.")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    #input jumlah perubahan stok
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus angka.")
        return

    #update
    stok_sekarang = stok_dict[kode]["stok"]

    if pilihan == "1":
        stok_dict[kode]["stok"] = stok_sekarang + jumlah
        print("Stok berhasil ditambah.")
    elif pilihan == "2":
        if stok_sekarang - jumlah < 0:
            print("Stok tidak cukup. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] = stok_sekarang - jumlah
        print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")
        return

    #otomatis simpan ke file
    simpan_stok(NAMA_FILE, stok_dict)

# ----------------------------------------
# Program Utama
# ----------------------------------------
def main():
    #membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        
        elif pilihan == "2":
            cari_barang(stok_barang)
        
        elif pilihan == "3":
            tambah_barang(stok_barang)
        
        elif pilihan == "4":
            update_stok(stok_barang)
        
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        
        elif pilihan == "0":
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()