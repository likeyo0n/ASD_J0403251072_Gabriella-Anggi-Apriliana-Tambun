#=================================================
#Nama: Gabriella Anggi Apriliana Tambun
#NIM : J0403251072
#Kelas : TPL/P1
#=================================================

#=================================================
#Latihan 1: Weighted Graph dan Perhitungan Jalur
#=================================================

#representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
#menghitung dua kemungkinan jalur dari A ke D
#mengambil bobot dari edge A ke B (4) ditambah bobot dari edge B ke D (5)
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
#mengambil bobot dari edge A ke C (2) ditambah bobot dari edge C ke D (1)
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

'''
pertanyaan analisis:
1. Berapa total bobot jalur A -> B -> D? 9
2. Berapa total bobot jalur A -> C -> D? 3
3. Jalur mana yang dipilih sebagai jalur terpendek? jalur kedua yaitu A -> C -> D
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
    Karena pada graf berbobot (weighted graph), jalur terpendek ditentukan oleh total jumlah bobot,
    bukan dari berapa banyak edge (langkah) yang dilewati. Jalur dengan banyak edge bisa saja
    memiliki total bobot yang lebih kecil dibandingkan jalur dengan sedikit edge.
'''