def celsius_to_fahrenheit(celsius):
    # Konversi Celsius ke Fahrenheit
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    # Konversi Celsius ke Kelvin
    return celsius + 273.15

def celsius_to_reamur(celsius):
    # Konversi Celsius ke Reamur
    return celsius * 4/5

def fahrenheit_to_celsius(fahrenheit):
    # Konversi Fahrenheit ke Celsius
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    # Konversi Fahrenheit ke Kelvin
    return (fahrenheit - 32) * 5/9 + 273.15

def fahrenheit_to_reamur(fahrenheit):
    # Konversi Fahrenheit ke Reamur
    return (fahrenheit - 32) * 4/9

def kelvin_to_celsius(kelvin):
    # Konversi Kelvin ke Celsius
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    # Konversi Kelvin ke Fahrenheit
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_reamur(kelvin):
    # Konversi Kelvin ke Reamur
    return (kelvin - 273.15) * 4/5

def reamur_to_celsius(reamur):
    # Konversi Reamur ke Celsius
    return reamur * 5/4

def reamur_to_fahrenheit(reamur):
    # Konversi Reamur ke Fahrenheit
    return reamur * 9/4 + 32

def reamur_to_kelvin(reamur):
    # Konversi Reamur ke Kelvin
    return reamur * 5/4 + 273.15

# Membuat judul program
print("=== Konversi Suhu ===")

# Meminta input suhu dari pengguna
suhu_input = float(input("Masukkan suhu: "))
satuan_input = input("Masukkan satuan suhu (C/F/K/R): ")

# Garis pemisah
print("=" * 30)

# Melakukan konversi berdasarkan satuan input
if satuan_input.upper() == 'C':
    print(f"{suhu_input} Celsius = {celsius_to_fahrenheit(suhu_input)} Fahrenheit")
    print(f"{suhu_input} Celsius = {celsius_to_kelvin(suhu_input)} Kelvin")
    print(f"{suhu_input} Celsius = {celsius_to_reamur(suhu_input)} Reamur")
elif satuan_input.upper() == 'F':
    print(f"{suhu_input} Fahrenheit = {fahrenheit_to_celsius(suhu_input)} Celsius")
    print(f"{suhu_input} Fahrenheit = {fahrenheit_to_kelvin(suhu_input)} Kelvin")
    print(f"{suhu_input} Fahrenheit = {fahrenheit_to_reamur(suhu_input)} Reamur")
elif satuan_input.upper() == 'K':
    print(f"{suhu_input} Kelvin = {kelvin_to_celsius(suhu_input)} Celsius")
    print(f"{suhu_input} Kelvin = {kelvin_to_fahrenheit(suhu_input)} Fahrenheit")
    print(f"{suhu_input} Kelvin = {kelvin_to_reamur(suhu_input)} Reamur")
elif satuan_input.upper() == 'R':
    print(f"{suhu_input} Reamur = {reamur_to_celsius(suhu_input)} Celsius")
    print(f"{suhu_input} Reamur = {reamur_to_fahrenheit(suhu_input)} Fahrenheit")
    print(f"{suhu_input} Reamur = {reamur_to_kelvin(suhu_input)} Kelvin")
else:
    print("Satuan suhu tidak valid. Masukkan 'C', 'F', 'K', atau 'R'.")

# Garis pemisah
print("=" * 30)
