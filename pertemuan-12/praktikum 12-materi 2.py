#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Implementasi Bellman Ford
#=================================================

import heapq
graph = {
    'A': {'B' : 4, 'C' : 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def bellman_ford(graph, start):
    #menginisialisasi jarak awal semua node dengan nilai tak terhingga (infinity)
    distances = {node: float('inf') for node in graph}
    #mengatur jarak ke node awal
    distances[start] = 0
    #relaksasi berulang
    #melakukan iterasi/pengulangan sebanyak (jumlah node - 1) kali. 
    #ini adalah syarat maksimum edge yang dilewati untuk jalur terpendek dalam graf tanpa siklus negatif.
    for _ in range(len(graph) - 1):
        #mengakses setiap node yang ada di dalam graf satu per satu
        for node in graph:
            #memeriksa setiap tetangga dari node yang sedang dicek beserta bobot/jaraknya
            for neighbor, weight in graph[node].items():
                #mengecek apakah jarak untuk menuju tetangga melalui node saat ini lebih kecil dari jarak yang sudah ada
                if distances[node] + weight < distances[neighbor]:
                    #jika lebih kecil, perbarui jarak tetangga tersebut dengan jarak baru yang lebih pendek (proses relaksasi)
                    distances[neighbor] = distances[node] + weight
    return distances
hasil = bellman_ford(graph, 'A')
print(hasil)