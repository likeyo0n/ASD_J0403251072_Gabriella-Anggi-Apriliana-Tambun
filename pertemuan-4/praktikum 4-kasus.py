#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Studi Kasus: Sistem Antrian Layanan Akademik
#Implementasi queue =>
#Front-> A -> B -> C -> Rear
#stack ==> Front -> B -> A -> None
#Enqueue: Memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue: Memindahkan pointer front (menghapus data dari depan)
#============================================

#1. mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim #menyimpan nim mahasiswa
        self.nama = nama #menyimpan nama mahasiswa
        self.next = None #pointer ke node berikutnya (awal)

#2. Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        #ketika queue kosong maka front = rear = none
        return self.front is None
    
    #menambahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama) #intantiasi
        #jika data baru masuk dari queue yang kosong maka date baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak ada Mhasiswa yang dilayani")
            return None

        #lihat data bagian front, simpan divariable data yang akan dihapus (dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):



        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program Utama
def main():

    #intantiasi queue
    q = queueAkademik()

    while True:
        print("===== Sistem Antrian Akademik=====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahankan ke Antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani: {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program Selesai. terima Kasih")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")

#penanda eksekusi file utama
if __name__== "__main__":
    main()
