class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    # fungsi untuk menambah node di akhir 
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    # menghapus node sesuai nilai
    def delete_node(self, key):
        temp = self.head
        
        # jika node yang ingin dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            print("Data berhasil dihapus!")
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        # jika data tidak ditemukan
        if temp is None:
            print("Data tidak ditemukan!")
            return
        
        prev.next = temp.next
        temp = None
        print("Data berhasil dihapus!")
        
    # menampilkan isi linked list
    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list kosong.")
            return
        
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")