def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan angka: "))
print(f"Faktorial dari {angka} adalah {faktorial(angka)}")
