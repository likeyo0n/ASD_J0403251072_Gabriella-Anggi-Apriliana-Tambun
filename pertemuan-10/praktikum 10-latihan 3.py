#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 5: Rotasi kiri pada BST tidak seimbang
#=================================================

#class node
class Node:
    def __init__(self, data):
        self.data = data #nilai pada node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

#fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

#fungsi rotasi kiri
def rotate_left(x):
    #x adalah root lama
    y = x.right #y adalah child kanan x
    T2 = y.left #subtree kiri milik y disimpan sementara
  
    #proses rotasi
    y.left =  x #x menjadi child kiri dari y
    x.right = T2 #child kanan x diganti dengan T2
  
    #y menjadi root baru
    return y

#================================
#program utama
#================================

#membuat tree yang tidak seimbang:
#10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

#melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)

'''
penjelasan
Kode tersebut dimulai dengan membuat class Node untuk menyimpan 
data node beserta child kiri dan kanan pada BST. Setelah itu, 
terdapat fungsi preorder() untuk menampilkan isi tree dengan 
urutan root-kiri-kanan, serta fungsi tampil_struktur() untuk 
menampilkan bentuk struktur tree agar lebih mudah dilihat. 
Pada bagian utama, program terlebih dahulu membuat BST yang tidak 
seimbang secara manual dengan susunan 10 → 20 → 30, sehingga 
semua node berada di sisi kanan. Selanjutnya, fungsi rotate_left() 
digunakan untuk melakukan rotasi kiri pada root lama (x), 
di mana child kanan (y) dijadikan root baru, lalu root lama 
dipindahkan menjadi child kiri dari y, sementara subtree kiri
milik y disimpan sementara dalam T2 dan dipasang kembali sebagai 
child kanan x. Setelah proses rotasi selesai, tree yang awalnya 
miring ke kanan menjadi lebih seimbang, dengan 20 sebagai root 
baru, 10 sebagai child kiri, dan 30 sebagai child kanan, kemudian 
hasil sebelum dan sesudah rotasi ditampilkan menggunakan fungsi 
preorder dan struktur tree.
'''