#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 3: Membuat Traversal Preorder
#=================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi traversal preorder : Root ==> left ==> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") #root: cetak isi node. end agar cetakannya bersebelahan
        preorder(node.left) #memanggil dirinya sendiri
        preorder(node.right)

#membuat tree
#membuat sebuah node root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal preorder
print("Hasil Traversal preorder: ")
preorder(root)

#penjelasan
'''
alur kode ini dimulai dengan merangkai struktur pohon dari atas
ke bawah ("A" sebagai akar, punya anak "B" dan "C", lalu "B" punya
anak "D" dan "E"), dilanjutkan dengan memanggil fungsi preorder yang
menggunakan teknik rekursi (fungsi yang memanggil dirinya sendiri)
untuk menjelajahi pohon tersebut dengan aturan Induk -> Kiri -> Kanan;
sehingga program akan mencetak akar "A" terlebih dahulu, menelusuri seluruh cabang
kiri dengan mencetak "B" lalu "D", mundur untuk mencetak cabang kanan "E", dan
terakhir bergeser menelusuri cabang kanan dari akar dengan mencetak "C",
menghasilkan cetakan akhir berurutan A B D E C di layar.
'''