#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 5: Tugas Mandiri: Buat Program MST dengan Kasus Baru
#=================================================
'''Kasus 2, kruskal'''
# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'RouterC', 'RouterD'), 
    (2, 'RouterA', 'RouterC'), 
    (3, 'RouterA', 'RouterB'), 
    (4, 'RouterB', 'RouterC'), 
    (5, 'RouterB', 'RouterD') 
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

print("Total biaya minimum =", total_weight)

'''
Pertanyaan Analisis
1. Kasus apa yang dipilih?
    kasus 2
2. Algoritma apa yang digunakan?
    kruskal
3. Edge mana saja yang dipilih dalam MST?
    ('RouterC', 'RouterD', 1), ('RouterA', 'RouterC', 2), ('RouterA', 'RouterB', 3)
4. Berapa total bobot MST? total bobot = 6
5. Mengapa edge tertentu tidak dipilih?
    menghindari cycle (agar tidka terjadi loop),
    node tsb sudah terhubung melalui jalur lain yang lebih murah,
    terakhir, algoritma hanya mengambil jalur minimum (prinsip mst)
'''