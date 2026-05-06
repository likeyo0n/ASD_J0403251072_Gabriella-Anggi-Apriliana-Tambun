#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Implementasi Dijkstra
#=================================================

import heapq
graph = {
    'A': {'B' : 4, 'C' : 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    #menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    #jarak node awal = 0
    distances[start] = 0
    #priority queue
    #menyimpan tuple (jarak, node_saat_ini) ke dalam antrean
    pq = [(0, start)]
    
    while pq:
        #mengeluarkan node dengan jarak terpendek dari priority queue
        current_distance, current_node = heapq.heappop(pq)
        #periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            #menghitung total jarak tempuh ke node tetangga melalui node saat ini
            distance = current_distance + weight
            
            #jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                #memperbarui jarak minimum untuk node tetangga tsb dengan nilai yang lebih kecil
                distances[neighbor] = distance
                #memasukkan node tetangga beserta jarak terbarunya kedalam priority queue untuk diproses lebih lanjut
                heapq.heappush(pq, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'A')
print(hasil)