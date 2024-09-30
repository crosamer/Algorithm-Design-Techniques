# Mohammad Adzka Crosamer / L0123083 / Informatika C
# Naufal Narendro Kusumo / L0123107 / Informatika C

uang = int(input("Jumlah uang: "))
jenis_koin = input("Masukkan koin (pisahkan dengan spasi): ")

coins = list(map(int, jenis_koin.split()))
coins.sort(reverse=True)

def kembalian(kebutuhan):
    result = [] 
    for koin in coins:
        while kebutuhan >= koin:
            result.append(koin)
            kebutuhan -= koin
            print(f"Memilih koin {koin}, sisa uang {kebutuhan}")
    
    if kebutuhan > 0:
        return None 
    return result  

result = kembalian(uang)
if result is None:
    print(f"\nUang {uang} tidak bisa ditukar dengan koin yang tersedia.")
else:
    print(f"\nUang {uang} bisa ditukar menjadi: {result}")