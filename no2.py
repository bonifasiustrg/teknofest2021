# no2 Penjumlahan Angka
def penjumlahan(masukan, target):
    daftar = list(masukan)
    for i in daftar:
        for j in daftar:
            i, j = int(i), int(j)  #casting i, j agar bisa dijumlahkan
            if i!=j and i + j == target: 
                x, y = daftar.index(str(i)), daftar.index(str(j)) #casting i, j agar indexnya bisa diakses
                if x<y: #agar data yg sama tidak berulang
                    hasil = [x, y]
                    break 
                print(hasil)


masukan, target = input().split(), int(input())
penjumlahan(masukan, target)