#=============================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#==============================================================

#==============================================================
#Latihan 5 Melengkapi Fungsi Merge
#==============================================================
'''
Jawaban no. 1 melengkapi agar menjadi ascending'''
def merge(left, right):
    result = []
    i = 0
    j = 0 

    #bandingkan elemen kiri dan kanan selama keduanya masih ada isi
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: #ambil nilai yang lebih kecil (ascending)
            result.append(left[i]) #masukkan ke result
            i += 1 #geser pointer ke kiri
        else:
            result.append(right[j]) #masukkan ke result 
            j += 1 #geser pointer ke kanan

    #jika masih ada sisa elemen di kiri, tambahkan semua
    result.extend(left[i:])

    #jika masih ada sisa elemen di kanan, tambahkan semua
    result.extend(right[j:])

    return result 

#====================
#Panggil Program 
#====================

left = [8, 14, 5]
right = [1, 7, 10, 45, 15]
hasil = merge(left, right)
print("Hasil Sorting: ", hasil)


"""
Jawaban No. 2 Jelaskan fungsi result.extend()!
fungsi tersebut berfungsi untuk menambahkan sisa elemen yang belum diproses 
ke dalam list result.
Hal ini dilakukan agar semua elemen tetap masuk ke hasil akhir setelah proses
perbandingan selesai.
"""