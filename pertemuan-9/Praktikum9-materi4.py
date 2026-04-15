#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 4: Membuat Traversal Inorder
#=================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat traversal inorder: left ==> root ==> right
def inorder(node):
    if node is not None:
        inorder(node.left) #memanggil dirinya sendiri untuk menyelam ke cabang kiri sampai habis
        print(node.data, end=" ") #setelah kiri selesai, cetak root
        inorder(node.right) #memanggil dirinya sendiri untuk menyelam ke cabang kanan sampai habis

#membuat tree
#membuat sebuah node root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal inorder
print("Hasil Traversal inorder: ")
inorder(root)

#penjelasan
'''
alur kode ini berfokus pada penelusuran pohon dengan aturan kunjungan Kiri ->
Induk -> Kanan (Inorder); di mana setelah struktur pohon selesai dibangun, fungsi inorder
akan menggunakan teknik rekursi untuk terus menyelam ke cabang paling kiri terlebih dahulu
hingga mentok di "D" lalu mencetaknya, kemudian mundur ke atas untuk mencetak induknya yaitu "B",
bergeser ke bawah untuk mencetak cabang kanan "E", mundur lagi hingga ke puncak untuk mencetak akar "A",
dan terakhir mengecek cabang kanan dari akar untuk mencetak "C", sehingga menghasilkan urutan akhir D B E A C di layar.
'''