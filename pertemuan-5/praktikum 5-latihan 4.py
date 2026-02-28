#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Latihan Rekursif
#Latihan 4: Kombinasi Huruf
#============================================

def kombinasi(n, hasil=""):
    #base case
    #kalau panjang teks kombinasi sudah sampai n, cetak lalu berhenti
    if len(hasil) == n:
        print(hasil)
        return
    #recrusive case
    #menambah huruf "A" terlebih dahulu sampai mentok
    kombinasi(n, hasil + "A")
    #kalau A sudah selesai, mundur dan coba rute B
    kombinasi(n, hasil + "B")

#mencari semua kombinasi A dan B sepanjanng 2 karakter
kombinasi(2)