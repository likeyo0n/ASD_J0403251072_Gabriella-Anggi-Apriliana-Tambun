#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Latihan Rekursif
#Latihan 3: Mencari Nilai Maksimum
#============================================

def cari_maks(data, index=0):
    #base case
    if index == len(data) - 1: #jika index sudah elemen terakhir (panjang list dikurang 1), kembalikan nilai tsb.
        return data[index]
    
    #recursive case
    maks_sisa = cari_maks(data, index + 1) #proses ini akan terus maju sampai ke elemen terakhir. hasil dari pemanggilan ini disimpan di maks_sisa

    #membandingkan angka di posisi sekarang dengan sisa list
    if data[index] > maks_sisa: 
        return data[index] #jika angka sekarang lebih besar, angka naik ke tahap selanjutnya
    else:
        return maks_sisa #jika tidak, maka maks_sisa yang menang
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))