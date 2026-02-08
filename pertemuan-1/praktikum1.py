#===========================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1A: Membaca seluruh isi file
#===========================================

#membuka file dengan mode read ("r")
with open("datamahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file=file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file)) #membaca tipe file
print("Jumlah Karakter", len(isi_file)) #menghitung jumlah karakter dalam file
print("Jumlah Baris", isi_file.count("\n")+1) # 

#membuka file per baris
print("===Membaca File Per Baris===")
jumlah_baris = 0
with open("datamahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan  karakter new line 
        print("Baris ke-",jumlah_baris)
        print("Isinya: ", baris)

#===========================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2: Parsing baris menjadi kolom data
#===========================================

with open("datamahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #data di pisahkan dengan tanda koma
        print("NIM: ",nim,"| Nama: ", nama, "| Nilai: ",nilai)

#===========================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3: Membaca File dan Menyimpan ke List
#===========================================

data_list = [] #list untuk menampung data mahasiswa

with open("datamahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #Simpan sebagai list "[nim,nama,nilai]"
        data_list.append([nim,nama,int(nilai)])

print("=== Data mahasiswa dalam List ===")
print(data_list)

print("=== Jumlah Record dalam List ===")
print("Jumlah Record", len(data_list))

print("=== Menampilkan Data Record Tertentu ===")
print("Contoh Record Pertama", data_list[0])

#===========================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4: Membaca File dan Menyimpan ke Dictionary
#===========================================

data_dict = {} #buat variabel buat dictionary
with open("datamahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictioary dengan key NIM
        data_dict[nim]={                #key
            "nama": nama,               #values
            "nilai" : int(nilai)        #values
        }
print("=== Data Mahasiswa dalam Dictionary ===")
print(data_dict)