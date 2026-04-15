#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 6: Struktur Organisasi Perusahaan
#=================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

def preorder(node):
    if node is not None:
        print(node.data, end=", ")
        preorder(node.left)
        preorder(node.right)

#membuat tree struktur organisasi
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

#child level 3
root.right.right = Node("Staff3")

#menjalankan traversal preorder
print("Hasil Struktur Organisasi: ")
preorder(root)

#penjelasan
'''
alur kode ini membangun sebuah hierarki organisasi
dengan "Direktur" sebagai pimpinan tertinggi (akar),
yang membawahi "Manajer A" di divisi kiri dan "Manajer B"
di divisi kanan; di mana Manajer A memimpin dua orang yaitu
"Staff1" dan "Staff2", sedangkan Manajer B hanya memimpin
satu orang di sisi kanan yaitu "Staff3". Setelah bagan terbentuk,
program menelusurinya menggunakan aturan Preorder (Atasan -> Kiri -> Kanan),
sehingga fungsi akan mencetak "Direktur" terlebih dahulu, turun menelusuri
seluruh divisi kiri dengan mencetak "Manajer A" beserta bawahannya "Staff1"
lalu "Staff2", kemudian fungsi berpindah menelusuri divisi kanan dengan mencetak
"Manajer B" dan langsung turun ke bawahannya yaitu "Staff3", menghasilkan urutan
akhir Direktur, Manajer A, Staff1, Staff2, Manajer B, Staff3, di layar.
'''