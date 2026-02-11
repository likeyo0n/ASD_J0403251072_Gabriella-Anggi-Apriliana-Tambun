class Node: 
    def __init__(self, data):
        self.data = data #menyimpan nilai/data dalam node
        self.next = None #pointer ke node berikutnya (awal = None)

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

     #menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data) # membuat node baru dengan data yang diberikan


        if not self.head: #jika list kosong
                self.head = new_node
                self.tail = new_node
                self.tail.next = self.head #circular
        else:
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = self.head  #circular kembali ke head

    #fungsi pencarian
    def search(self, key):
        if not self.head:
            return None
        
        temp = self.head #membuat node baru dengan data yang diberikan

        #cek head dulu
        if temp.data == key:
            return True
        
        temp = temp.next
        while temp != self.head: #ulangi sampai kembali lagi ke head (karena circular)
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
# ================= PROGRAM UTAMA =================


cll = CircularSinglyLinkedList() # membuat objek circular linked list

#input elemen (pisahkan dengan koma)
data_input = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

if data_input.strip() != "":
    data_list = data_input.split(",")
    for item in data_list:
        cll.insert_at_end(int(item.strip())) # masukkan ke linked list

key = int(input("Masukkan elemen yang ingin dicari: "))

#cek kondisi kosong
if not cll.head:
    print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
else:
    if cll.search(key): # panggil fungsi search
        print(f"Elemen {key} ditemukan dalam Circular Linked List.")
    else:
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")