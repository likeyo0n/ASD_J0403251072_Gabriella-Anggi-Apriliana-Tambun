#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 3: Implementasi  Bellman-Ford
#=================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}
def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances
hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

'''
Pertanyaan Analisis
1. Berapa bobot langsung dari A ke B? 5
2. Berapa total bobot jalur A -> C -> B? 2
    Total bobotnya adalah 2 (didapat dari bobot A -> C yaitu 4, ditambah bobot C -> B yaitu -2; sehingga 4 + (-2) = 2)
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? jalur A -> C -> B
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
    Karena algoritma ini mengevaluasi semua edge secara berulang, sehingga jarak tetap bisa diperbarui/dikoreksi jika melewati bobot negatif.
5. Apa yang dimaksud dengan proses relaksasi edge?
    Proses memperbarui jarak ke suatu node jika ditemukan jalur baru yang nilainya lebih pendek.
6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
    Bellman-Ford bisa memproses edge berbobot negatif namun kinerjanya lebih lambat, sedangkan Dijkstra tidak bisa memproses bobot negatif namun kinerjanya lebih cepat.
'''