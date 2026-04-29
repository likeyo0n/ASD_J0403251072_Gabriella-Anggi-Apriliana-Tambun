#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Implementasi DFS
#=================================================

#reprentasi graph
graph = {
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['F', 'G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
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

    #perikasa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan fungsi rekursif ke tetangga tsb
            dfs(graph,neighbor,visited)
#set visited
visited = set()

#menjalankan dari dfs
dfs(graph,"A",visited)