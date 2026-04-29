#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 1
#=================================================

from collections import deque

graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    #Fungsi untuk melakukan penelusuran dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph
    # start : node awal penelusuran
    
    #queue digunakan untuk menyimpan node yang akan diproses/dibaca
    queue = deque()
    
    #variabel visited : menyimpan node yang sudah diproses/dibaca
    visited = set()
    
    #masukkan node awal ke queue 
    queue.append(start)
    
    #tandai node awal yang sudah masuk queue sebagai node yang sudah dikunjungi
    visited.add(start)
    
    while queue:
        # mengambil node paling depan dari queue
        node = queue.popleft()
        #Tampilkan node yang sedang dikunjungi
        print(node, end=' ' )
        
        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukkan tetangga ke queue untuk diproses
                queue.append(neighbor)

print("BFS dari Rumah:")
# menjalankan BFS dari node A
bfs(graph, 'Rumah')

'''
Pertanyaan Analisis
1. Node mana yang dikunjungi pertama? Rumah karena rumah adalah node awal
2. Mengapa BFS cocok untuk mencari jalur terdekat? karena BFS mencari secara bertahap atau level demi level.
    jadi, target yang pertama kali ditemukan otomatis rute dengan jumlah langkah paling sedikit 
3. Apa perbedaan urutan BFS jika struktur graph diubah?
    -jika tambah edge, maka titik yang akan dikunjungi lebih cepat karena ada jalan pintas
    -jika hapus edge, maka titik yang dikunjungi lebih lambat (jalur memutar), atau bisa tidak terjangkau sama sekali jika graph terputus
    -jila urutan antrean bergeser, maka siapa yang dicek lebih dulu di dalam queue berubah menyesuaikan koneksi tetangga yang baru
'''