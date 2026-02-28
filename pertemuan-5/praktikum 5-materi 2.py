#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Materi Rekursif: call Stack
#Tracing bilangan (masuk-keluar)
#input 3 
#Masuk 3 - 2 - 1
#Keluar 1 - 2 - 3
#============================================

def hitung(n):
    
    #base case
    if n == 0: 
        print("Selesai")
        return
    
    print("Masuk: ",n)
    hitung(n-1) #recursive case
    print("Keluar:", n)

print("====Program Tracing=====")
hitung(3)