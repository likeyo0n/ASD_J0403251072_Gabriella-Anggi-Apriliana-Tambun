#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Materi Rekursif
#Contoh Backtracking 1: Kombinasi Biner (n)
#============================================

def biner(n,hasil=""):
    #base case: jika panjang string sudah n, cetak hasil
    if len(hasil)==n:
        print(hasil)
        return

    #choose + eksplore: tambah '0'
    #angka 0 akan ditambahkan sampai batas base case
    biner(n, hasil + "0")

    #choose + eksplore: tambah '1'
    #setelah mentok di 0, mundur satu langkah dan mencoba rute 1
    biner(n, hasil + "1")

biner(3)