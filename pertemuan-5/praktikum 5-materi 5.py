#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Materi Rekursif
#Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
#============================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    #Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas: #jika jumlah angka 1 melewati batas
        return
    
    #base case
    if len(hasil)==n: #jika panjang kombinasi sudah pas (n digit)
        print(hasil)
        return
    #pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1) #karena ditambah 0, jumlah_1 nilainya tetap
    #pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) #karena ditambah 1, jumlah_1 harus ditambah 1 untuk memantau batas 

#biner sepanjang 4 digit, dengan maksimal dua angka 1
biner_batas(4, 2)