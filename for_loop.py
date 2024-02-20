banyak  = int(input("Berapa banyak data yang kamu inginkan : "))
nama = []
umur = []
jumlah = range(0 , banyak);

for i in range(0 , banyak):
    print(f"data ke {i}")
    input_nama = input("masukan nama : ")
    input_umur = int(input('masukan umur : '));

    nama.append(input_nama)
    umur.append(input_umur)
    
    
for i in range(0 , len(nama)):
    print(f"Data Nama : {nama[i]} berumur : {umur[i]}")
    