harga_supperrior1_2h = 100000
harga_supperrior3_4h = 150000
harga_supperrior5h = 200000

harga_deluxe1_2h = 250000
harga_deluxe3_4h = 300000
harga_deluxe5h = 350000

harga_Premium1_2h = 400000
harga_Premium3_4h = 450000
harga_Premium5h = 500000


# SELAMAT DATANG DI UBSI HOTEL.
print("Silahkan Pilih--")
print("|Penginapan|Superrior       |Deluxe         |Premium      |")
print("|----------|----------------|---------------|-------------|")
print("|1-2hari   |100.000/night   |250.000/night  |400.000/night|")
print("|3-4hari   |150.000/night    |300.000/night  |450.000/night|")

print("|5hari     |200.000/night    |350.000/night  |500.000/night|")
print("|----------|----------------|---------------|-------------|")

while True:
    cust = input("masukkan nama :")
    print("Tipe Kamar")
    print("1. Superrior")
    print("2. Deluxe")
    print("3. Premium")
    tipe = int(input("Tipe : "))
    lama_inap = int(input("Masukan Lama Menginap : "))

    if tipe == 1:   
        tipe_kamar = "Superrior"
        if lama_inap == 1 or lama_inap == 2:
            harga_kamar = harga_supperrior1_2h
        elif lama_inap == 3 or lama_inap == 4:
            harga_kamar = harga_supperrior3_4h
        elif lama_inap >= 5:
            harga_kamar = harga_supperrior5h

    elif tipe == 2:
        tipe_kamar  = "Deluxe"
        if lama_inap == 1 or lama_inap == 2:
            harga_kamar = harga_deluxe1_2h
        elif lama_inap == 3 or lama_inap == 4:
            harga_kamar = harga_deluxe3_4h
        elif lama_inap >= 5:
            harga_kamar = harga_deluxe5h

    elif tipe == 3:
        tipe_kamar = "Premium"
        if lama_inap == 1 or lama_inap == 2:
            harga_kamar = harga_Premium1_2h
        elif lama_inap == 3 or lama_inap == 4:
            harga_kamar = harga_Premium3_4h
        elif lama_inap >= 5:
            harga_kamar = harga_Premium5h
            
    total_harga = harga_kamar * lama_inap
    
    # struk UBSI Hotel

    print("====== Pembayaran ======")
    print ("Nama : ", cust)
    print ("Tipe kamar : ", tipe_kamar)
    print ("Lama Menginap : ", lama_inap)
    print ("harga penginapan", harga_kamar)
    print ("total pembayaran : ","Rp", total_harga,",00" )


    ulangi = input("Apakah anda ingin memesan ulang? (ya/tidak):")
    if ulangi.lower() != "ya":
        break