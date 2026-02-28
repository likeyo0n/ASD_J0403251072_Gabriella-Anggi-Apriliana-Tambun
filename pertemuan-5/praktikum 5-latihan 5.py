#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Latihan Rekursif
#Latihan 5: Generator PIN
#============================================

def buat_pin(panjang, hasil=""):
    #base case
    #jika panjang kombinasi PIN sudah mencapai target, cetak dan berhenti
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    #recrusive case
    for angka in ["0","1","2"]: #loop ini otomatis akan mengeksplorasi angka "0" sampai mentok, lalu mundur untuk mencoba "1", dan seterusnya
        buat_pin(panjang, hasil + angka)

#membuat PIN dengan 3 digit
buat_pin(3)