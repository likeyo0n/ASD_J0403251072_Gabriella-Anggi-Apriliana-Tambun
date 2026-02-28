#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Latihan Rekursif
#Latihan 2: Tracing Rekursi
#============================================

def countdown(n):
    #base case
    if n == 0:
        print("Selesai")
        return
    
    #cetak angka saat fungsi baru dipanggil
    print("Masuk:", n)
    #recursive case
    countdown(n - 1) #panggil fungsi lagi dengan n dikurangi 1
    #cetak angka setelah fungsi diatas selesai
    print("Keluar:", n)
#mulai hitung mundur dari 3
countdown(3)