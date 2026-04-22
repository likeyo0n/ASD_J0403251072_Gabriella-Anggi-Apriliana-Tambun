#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 4: Membuat BST yang tidak seimbang
#=================================================

#Class Node untuk menyimpan data BST

class Node:
    def __init__(self, data):
        self.data = data #nilai pada node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi insert untuk BST
def insert(root, data):
    #jika root kosong, buat node baru
    if root is None:
        return Node(data)
    #jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    #jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

#fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

#fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

#==================================
#program utama
#==================================
root = None

#data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

'''
penjelasan
kode tersebut dimulai dengan membuat class Node untuk menyimpan nilai data beserta
anak kiri dan kanan pada Binary Search Tree (BST). Setelah itu, fungsi insert()
digunakan untuk memasukkan data ke dalam tree dengan aturan BST, yaitu jika nilai 
lebih kecil dari root maka masuk ke kiri, sedangkan jika lebih besar masuk ke kanan, 
dan proses ini dilakukan secara rekursif sampai menemukan posisi yang kosong.
Selanjutnya, pada program utama variabel root diinisialisasi None, lalu 
data [10, 20, 30] dimasukkan secara berurutan menggunakan perulangan for. Karena data
dimasukkan dari kecil ke besar, setiap nilai baru selalu masuk ke sisi kanan sehingga
tree menjadi tidak seimbang atau condong ke kanan. Setelah tree terbentuk, fungsi preorder()
digunakan untuk menampilkan urutan node dengan pola root-kiri-kanan, sedangkan fungsi tampil_struktur()
digunakan untuk memperlihatkan bentuk struktur BST agar terlihat posisi root, anak kiri, dan anak
kanan secara jelas.
'''