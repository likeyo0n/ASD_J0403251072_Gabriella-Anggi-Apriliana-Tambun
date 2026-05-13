#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 1: Konsep Spanning Tree
#=================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
    print(edge)
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

'''
Pertanyaan Analisis
1. Apa perbedaan graph awal dan spanning tree?
    graph awal menampilkan seluruh jalur yang memungkinkan serta terdapat cycle dan jumlah edge yang besar. 
    sedangkan spanning tree menghubungkan jalur tanpa adanya cycle.
2. Mengapa spanning tree tidak boleh memiliki cycle?
    Karena ini merupakan sistem pohon yang harus melewati satu jalur saja. Kalau ada cycle yang melalui jalur sama dan 
    kembali ke titik asal, maka ini sama saja dengan graph biasa.
3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
    Karena tujuannya adalah efisiensi. Jadi, kita akan mengambil jumlah jalur yang paling minimal.
    Jika sebuah graph memiliki 4 titik, maka butuh 3 garis untuk berjalan. 
'''