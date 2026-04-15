#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 1: Membuat Node
#=================================================

#class node digunakan untuk dasar dari tree
#mendefinisikan class node
class Node:
    def __init__(self, data): #fungsi yang otomatis dijalankan saat node baru diciptakan
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat sebuah node root (titik paling atas atau awal)
root = Node("A") 

#memanggil sekaligus menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

#penjelasan: 
'''
awalnya membuat bentuk dasar sebuah node, program membuat node pertama yang isinya "A"
dan menjadikannya sebagai akar tertinggi (root), kemudian program mencetak 
isi akar tersebut dengan cabang kanan kirinya yang masih kosong.
'''