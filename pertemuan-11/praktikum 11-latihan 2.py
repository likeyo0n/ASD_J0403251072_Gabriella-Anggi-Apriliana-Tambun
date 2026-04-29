#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 2
#=================================================

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D':[],
    'E':[],
    'F':[]
}

def dfs(graph,node,visited):
    #fungsi untuk melkukan penelusuran graph menggunakan DFS
    #graph: dist yang menyimpan graph
    #node: menyimpan node yang dikunjungi
    #visited: menyimpan node yang sudah dikunjungi
    
    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan fungsi rekursif ke tetangga tsb
            dfs(graph,neighbor,visited)
#set visited
visited = set()

print("DFS dari A:")
#menjalankan dari dfs
dfs(graph,'A',visited)

'''
Pertanyaan Analisis
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
    karena DFS menggunakan cara kerja stack (last in, first out)
2. Apa yang terjadi jika urutan neighbor diubah?
    jalur atau urutan kunjungannya akan berubah. cabang mana yang dieksplor lebih dulu jadi berbeda,
    sehingga bentuk pohon pencariannya (spanning tree) juga berbeda.
    Namun, jika graf tersebut saling terhubung, hasil akhirnya sama dan semua titik tetap akan terkunjungi
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
    -arah: BFS menyebar melebar, DFS menelusuri mendalam
    -Jalur Terpendek: BFS menjamin rute terpendek, DFS tidak
    -Sistem: BFS pakai queue (antrean), DFS pakai stack (tumpukan)
'''