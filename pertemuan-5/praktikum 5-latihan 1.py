#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Latihan Rekursif
#Latihan 1: Rekursi Pangkat
#============================================

def pangkat(a, n):
    #base case
    if n == 0: #kalau pangkatnya 0, hasilnya akan 1
        return 1
    
    #recusive case
    return a*pangkat(a, n-1) #mengalikan angka dasar (a) dengan pangkat yang n-nya dikurangi 1. ulang hingga n menjadi 0

print(pangkat(2, 4)) #berarti 2 pangkat 4