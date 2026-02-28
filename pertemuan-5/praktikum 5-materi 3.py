#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Materi Rekursif: Menjumlahkan Elemen List
#============================================
def jumlah_list(data, index=0):
    #base case
    if index == len(data): #jika index sudah sama dengan panjang list
        return 0 #maka sudah elemen terakhir, mengembalikan 0 agar tidak mengubah hasik
    #recursive case
    return data[index] + jumlah_list(data, index+1)


print("=====Program Jumlah Data List=====")
print(jumlah_list([2,4,5]))