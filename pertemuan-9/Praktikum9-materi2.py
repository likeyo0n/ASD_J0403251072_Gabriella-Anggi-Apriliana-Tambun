#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 2: Membuat Binary Search Tree Sederhana
#=================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat sebuah node root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2, anak dari B
root.left.left = Node("D")
root.left.right = Node("E")

#membuat child level 3, anak dari C
root.right.left = Node("F")
root.right.right = Node("G")

#menampilkan isi node
print("Data pada root", root.data) #mengambil dan mencetak nilai pada root
print("Child kiri root", root.left.data) #mengakses root lalu berjalan ke cabang kiri, lalu mencetak nilai node tersebut
print("Child kanan root", root.right.data) #mengakses root lalu berjalan ke cabang kanan, lalu mencetak nilai node tersebut
print("Child kiri dari B: ", root.left.left.data) #mengakses root lalu berjalan ke cabang kiri (B), lalu ke kiri, lalu mencetak nilai node tersebut
print("Child kanan dari B: ", root.left.right.data) #mengakses root lalu berjalan ke cabang kanan (B), lalu ke kanan lagi, lalu mencetak nilai node tersebut
print("Child kiri dari C: ", root.right.left.data) #mengakses root lalu berjalan ke cabang kanan (C), lalu ke kiri, lalu mencetak nilai node tersebut
print("Child kanan dari C: ", root.right.right.data) #mengakses root lalu berjalan ke cabang kanan (C), lalu ke kanan lagi, lalu mencetak nilai node tersebut

#penjelasan:
'''
awalnya membuat satu titik awal (root) yaitu A, lalu memberinya
dua child yaitu B dan C. setelah itu memberi child lagi ke masing-masing
B (D dan E) dan C (F dan G). kemudian terakhir mengecek kembali setiap
titik dengan menelusuri jalur dari atas (root) ke bawah.
'''