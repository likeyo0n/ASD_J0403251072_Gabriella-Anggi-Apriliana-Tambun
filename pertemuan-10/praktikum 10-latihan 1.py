#================================================= 
#Nama: Gabriella Anggi Apriliana Tambun
#NIM: J0403251072
#Kelas: TPL B1
#Latihan BST
#=================================================

#=================================================
#latihan 1: Node dan Insert BST
#=================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,data): #fungsi untuk memasukkan data baru  ke dalam BST sesuai aturan
    if root is None: #jika titik yang dituju masih kosong, buat Node baru di posisi tersebut
        return Node(data)

    if data <root.data: #jika data baru lebih kecil dari data root saat ini, lempar/masukkan ke cabang kiri
        root.left = insert(root.left, data)
            
    elif data > root.data: #jika lebih besar
        root.right = insert(root.right, data)
            
    return root
    
#Mengisi data BST
root =  None
data_list = [50,30,70,20,40,50,80]

for data in data_list: #perulangan untuk memasukkan semua angka dari data_list
    root = insert(root, data)
    
print("BST berhasil dibuat")


#=================================================
#Latihan 2 : Traversal Inorder
#=================================================

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        
print("Hasil Inorder : ")
inorder(root)


#=================================================
#Latihan 3 : Search di BST 
#=================================================
#untuk mencari angka (key) didalam pohon
def search(root,key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    elif key < root.data:
        return search(root.left, key)
    
    else: 
        return search(root.right, key)
    
#uji pencarian
key = 40 #menentukan angka yang ingin dicari
if search(root, key):
    print("Data ditemukan")
else: 
    print("Data tidak ditemukan")


#penjelasan
'''
kode ini adalah BST, dimana ketika fungsi insert dipanggil, angka pertama (50) dijadikan root, lalu angka
berikutnya disaring, kalau lebih kecil di lempar kecabang kiri, kalau lebih besar ke cabang kanan, dan kalau
ada angka duplikat bakal langsung diskip. saat manggil fungsi inorder untuk nampilin data, hasilnya bakal
otomatis ke-print secara terurut dari terkecil ke terbesar.
'''