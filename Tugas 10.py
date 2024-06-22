def kalkulator(a, b, operasi):
    if operasi == '+':
        return a + b
    elif operasi == '-':
        return a - b
    elif operasi == '*':
        return a * b
    elif operasi == '/':
        return a / b
    else:
        return "Operasi tidak valid"

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")
hasil = kalkulator(angka1, angka2, operasi)
print(f"Hasil: {hasil}")