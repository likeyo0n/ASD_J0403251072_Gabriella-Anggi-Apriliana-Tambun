#============================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#============================================

#============================================
#Implementasi Dasar: Node pada Linked List
#============================================

#Membuat class Node (merupakan unit dasar dari Linked List)
class Node:
    def __init__(self,data): #konstruktor
        self.data = data #menyimpan nilai / data
        self.next = None #pointer ke note berikutnya (awal=none)

#1. Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2. Menghubungkan Node : A-> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

#3. Menentukan node pertama (head)
head = nodeA

#4. Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#============================================
#Implementasi Dasar: Linked List + Insert Awal
#============================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self,data): #push dalam stack
        #1. buat node baru
        nodeBaru = Node(data) #panggil class node

        #2. node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3. head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack untuk menyoroti head
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah :", data_terhapus)

    def tampilkan(self): #implementasi traversal
        current = self.head
        while current is not None:
            print (current.data)
            current = current.next

print("=====List Baru=====")
ll = LinkedList() #instantiasi ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()