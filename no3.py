# no3 Total Kemunculan
def total_muncul():
    masukan = input().split() 
    kamus = {}
    # menghitung jlh masukan
    for i in masukan:
        jlh = masukan.count(i)
        list_to_set = set(masukan)
        masukan_nonredundan = list(list_to_set)
        # menambahkan ke kamus tanpa ada data double
        for j in masukan_nonredundan:
            if i == j:
                kamus[j] = jlh
    # urutkan kamus berdasarkan valuenya
    sortbyvalue = {k: v for k, v in sorted(kamus.items(), key=lambda v: v[1])}
    for k in sortbyvalue:
        print(k, ': ', sortbyvalue[k],sep = '')
    
    # # urutkan kamus berdasarkan keynya
    # sortbykey = {k: v for k, v in sorted(kamus.items())}
    # for k in sortbykey:
    #     print(k, ': ', sortbykey[k], sep = '')
total_muncul()