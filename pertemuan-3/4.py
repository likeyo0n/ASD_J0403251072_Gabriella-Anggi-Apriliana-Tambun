class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  #tambahkan pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: #jika linked list kosong
            self.head = new_node
            self.tail = new_node #tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node #sambungkan tail ke node baru
            self.tail = new_node #update tail ke node baru

    def display(self):
        current = self.head
        
        #jika list kosong
        if current is None:
            print("kosong")
            return

        #perulangan
        while current is not None:
            print(current.data, end="")
            print(" -> ", end="")
            current = current.next #pindah ke node berikutnya
        print("null") #penutup di paling belakang

def gabung_linked_list(list1, list2):
    list_baru = LinkedList()

    current = list1.head
    while current is not None:
        list_baru.insert_at_end(current.data)
        current = current.next

    current = list2.head
    while current is not None:
        list_baru.insert_at_end(current.data)
        current = current.next

    return list_baru

def buat_list_dari_input(urutan):
    ll = LinkedList()
    print(f"\n--- Input Linked List {urutan} ---")
    print("Masukkan angka (pisahkan dengan spasi). Tekan Enter jika selesai.")
    
    data_input = input(f"Isi List {urutan}: ")
    
    #cek jika kosong
    if data_input == "":
        return ll

    #memecah input menjadi angka
    angka_list = data_input.replace(',', ' ').split()
    
    for item in angka_list:
        ll.insert_at_end(int(item))
            
    return ll

# ==========================================
# MAIN PROGRAM
# ==========================================


list1 = buat_list_dari_input("1")
list2 = buat_list_dari_input("2")

print("\n----------------Hasil----------------")
print("Linked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

print("Linked List setelah digabungkan:", end=" ")
hasil_gabungan = gabung_linked_list(list1, list2)
hasil_gabungan.display()