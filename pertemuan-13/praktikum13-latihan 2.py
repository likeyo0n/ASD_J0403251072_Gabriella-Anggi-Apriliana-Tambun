#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 2: Implementasi Algoritma Kruskal
#=================================================

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = [] 
total_weight = 0 

connected = set() 

for weight, u, v in edges: 
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 

        mst.append((u, v, weight)) 
        total_weight += weight 

        connected.add(u) 
        connected.add(v) 

print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 

print("Total bobot =", total_weight)

'''
Pertanyaan Analisis
1.  Edge mana yang dipilih pertama kali?
    Edge antara node C dan D dengan bobot 1, karena edge tersebut memiliki
    bobot yang paling kecil dibandingkan dengan edge yang lainnya.

2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
    Karena tujuan dari Minimum Spanning Tree (MST) adalah menghubungkan semua node
    dengan total bobot seminimum mungkin. Dengan memilih bobot terkecil terlebih dahulu, 
    total biaya atau jarak keseluruhan dapat dibuat lebih kecil.

3. Berapa total bobot MST yang dihasilkan?
    Total bobot MST yang dihasilkan adalah 6. Nilai tersebut diperoleh dari penjumlahan
    bobot edge yang terpilih, yaitu 1, 2, dan 3.

4. Mengapa edge tertentu tidak dipilih? 
    Edge tertentu tidak terpilih karena semua node sudah berhasil terhubung menggunakan
    edge dengan bobot yang lebih kecil. Jika edge tambahan tetap ditambahkan, maka total bobot 
    akan jadi jauh leboh besar dan akan membentuk cycle sehingga edge tersebut tidak diperlukan
    dalam MST.
'''