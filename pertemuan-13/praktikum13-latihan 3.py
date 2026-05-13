#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 3: Implementasi Algoritma Prim
#=================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}
def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight
mst, total = prim(graph, 'A')
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

'''
Pertanyaan Analisis
1. Node awal apa yang digunakan? Node 'A'
2. Edge mana yang dipilih pertama kali? ('A', 'C') dengan bobot 2
3. Bagaimana Prim menentukan edge berikutnya? Algoritma selalu mengambil edge dengan bobot terkecil
    yang menghubungkan node yang sudah dikunjungi dengan node yang belum di kunjungi
4. Berapa total bobot MST yang dihasilkan? A ke C = 2, C ke D = 1, D ke B = 3. Jadi total bobotnya 6
5. Apa perbedaan pendekatan Prim dan Kruskal? kalau prim dimulai dari satu titik, lalu ke titik terdekat yang paling kecil bobotnya sampai semua terhubung.
    kalau kruskal mengurutkan semua edge dari yang terkecil, lalu diambil satu persatu selama tidak membentuk cycle
'''