#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 5: Rotasi kanan pada BST tidak seimbang
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

#fungsi rotasi kanan
def rotate_right(y):
    #x adalah root lama
    x = y.left #x adalah child kiri y
    T2 = x.right #subtree kanan milik x disimpan sementara
  
    #proses rotasi
    x.right = y  #x menjadi child kanan dari x
    y.left = T2 #child kiri y diganti dengan T2
  
    #y menjadi root baru
    return x

#================================
#program utama
#================================

#membuat tree yang tidak seimbang:
#30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

#melakukan rotasi kanan pada root
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)

'''
penjelasan
Kode tersebut diawali dengan pembuatan class Node yang digunakan untuk 
menyimpan nilai data serta child kiri dan kanan pada BST. Selanjutnya 
terdapat fungsi preorder() untuk menampilkan isi tree dengan urutan 
root-kiri-kanan, serta fungsi tampil_struktur() untuk memperlihatkan 
bentuk struktur tree agar posisi setiap node terlihat jelas. Pada bagian 
program utama, tree dibuat secara manual dalam keadaan tidak seimbang 
dengan susunan 30 → 20 → 10, sehingga semua node berada di sisi kiri. 
Setelah itu, fungsi rotate_right() digunakan untuk melakukan rotasi kanan 
pada root lama (y), di mana child kiri (x) dijadikan root baru, lalu root 
lama dipindahkan menjadi child kanan dari x, sedangkan subtree kanan 
milik x disimpan sementara dalam T2 dan dipasang kembali sebagai child 
kiri y. Setelah rotasi selesai, tree yang awalnya miring ke kiri menjadi 
lebih seimbang, dengan 20 sebagai root baru, 10 sebagai child kiri, dan 
30 sebagai child kanan, kemudian hasil sebelum dan sesudah rotasi ditampilkan 
menggunakan fungsi preorder dan struktur tree.
'''