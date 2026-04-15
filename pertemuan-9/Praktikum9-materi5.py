#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 5: Membuat Traversal Postorder
#=================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat traversal postorder: left ==> right ==> root
def postorder(node):
    if node is not None:
        postorder(node.left) #memanggil dirinya sendiri untuk menyelam ke cabang kiri sampai mentok
        postorder(node.right) #memanggil dirinya sendiri untuk menyelam ke cabang kanan sampai mentok
        print(node.data, end=" ") #setelah child kanan dan kiri selesai, baru cetak root

#membuat tree
#membuat sebuah node root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal postorder
print("Hasil Traversal postorder: ")
postorder(root)

#penjelasan
'''
alur kode ini menelusuri pohon dengan aturan kunjungan
Kiri -> Kanan -> Induk (Postorder); di mana program akan
menggunakan teknik rekursi untuk menyelam terus ke cabang
paling kiri hingga mentok dan mencetak "D", kemudian
mengecek cabang kanan dari induknya untuk mencetak "E",
barulah naik untuk mencetak sang induk "B", lalu setelah
seluruh sisi kiri pohon selesai program akan berpindah
menelusuri cabang kanan dari akar untuk mencetak "C", dan
sebagai penutup program akan kembali ke titik puncak untuk
mencetak akar "A", sehingga menghasilkan urutan akhir D E B C A di layar.
'''