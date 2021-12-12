# no1 Angka Muncul Sekali
def kemunculan(kata):
    karakter = list(kata)
    muncul_sekali = []
    for i in karakter:
        jlh = karakter.count(i)  # hitung jumlah karakter i 
        if jlh==1:
            i = int(i)
            muncul_sekali.append(i) # tambahkan i ke list muncul_sekali
    return print(muncul_sekali)
        
kata = input()
kemunculan(kata)
