#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 2: Implementasi Djikstra
#=================================================

import heapq
# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
def dijkstra(graph, start):
    '''
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    '''
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

'''
Pertanyaan Analisis
1. Berapa jarak terpendek dari A ke B? 4
2. Berapa jarak terpendek dari A ke C? 2
3. Berapa jarak terpendek dari A ke D? 3
4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
    Karena total akumulasi bobot pada jalur A -> C -> D (2 + 1 = 3) jauh lebih kecil
    dibandingkan dengan total bobot pada jalur A -> B -> D (4 + 5 = 9)
5. Apa fungsi priority_queue dalam algoritma Dijkstra?
    untuk mengurutkan dan selalu mengambil node dengan jarak terpendek yang tersedia
    saat ini untuk diproses lebih dulu (bersifat greedy). Hal ini membuat pencarian
    jalur terpendek menjadi lebih cepat dan efisien
6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
    Algoritma Dijkstra mengasumsikan bahwa saat sebuah node dikeluarkan dari priority queue,
    jarak ke node tersebut sudah final (tidak bisa lebih pendek lagi). Jika ada edge berbobot negatif,
    ada kemungkinan jarak yang sudah dianggap "final" tersebut ternyata masih bisa berkurang di kemudian langkah,
    sehingga hasil akhirnya menjadi tidak akurat (salah perhitungan).
    Untuk graf dengan bobot negatif, algoritma Bellman-Ford adalah solusi yang tepat.
'''