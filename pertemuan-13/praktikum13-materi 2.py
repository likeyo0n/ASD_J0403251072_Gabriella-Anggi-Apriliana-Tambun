#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Materi 1: Implementasi Prim
#=================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}
def prim(graph, start):
    visited = set([start]) #set untuk mencatat node mana saja yang udah masuk ke mst
    edges = []

    for neighbor, weight in graph[start].items(): #memasukkan semua edge dari titik mulai ke dalam priority queue
        heapq.heappush(edges, (weight, start, neighbor))
    mst = [] #list untuk menimpan jalur yang terpilih menjadi mst
    total_weight = 0 #var untuk menjumlahkan total bobot mst
    while edges: #selama masih ada edge yang bisa di evaluasi di dalam heap 
        weight, u, v = heapq.heappop(edges) #ambil edge dengan bobot paling kecil
        if v not in visited: #cek apakah node tujuan (v) sudah pernah dikunjungi atau belum, untuk mencegah terjadinya loop (cycle)
            visited.add(v) #tandai v jika udah dikunjungi
            mst.append((u, v, weight)) #tambanhakn jalur ke dalam hasil mst
            total_weight += weight #tambahkan bobotnya ke total
            for neighbor, w in graph[v].items(): #cari semua tetangga dari node yang baru saja ditambahkan (v)
                if neighbor not in visited: #jika tetangga tsb belum masuk mst, masukkan ke antrian heap
                    heapq.heappush(edges, (w, v, neighbor)) 

    return mst, total_weight
mst, total = prim(graph, 'A')
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)
