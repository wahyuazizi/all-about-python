# Latihan conversi satuan temperatur

# Program konversi celcius ke satuan lain

print("\nProgram Konversi Temperatur")

# celcius = float(input('Masukkan suhu celcius: '))
# print(f"Suhu adalah: {celcius}")

# # Reamur
# reamur = (4/5) * celcius
# print(f"Suhu reamur: {reamur}")

# # Fahrenheit
# fahrenheit = ((9/5) * celcius) + 32
# print(f"Suhu Fahrenheit: {fahrenheit}")

# # Kelvin
# kelvin = celcius + 273
# print(f"Suhu Kelvin: {kelvin}")

fahrenheit2 = float(input(f"Masukkan nilai F: "))
print(f"suhu F: {fahrenheit2}")

# Fahrenheit ke Kelvin
F_to_K = ((5/9) * (fahrenheit2 - 32)) + 273
print(f"Suhu F ke K: {F_to_K}")

# Kelvin ke Fahrenheit
kelvin2 = float(input(f"Masukkan nilai K: "))
K_to_F = ((kelvin2 - 273) * (9/5)) + 32
print(f"Nilai K ke F: {K_to_F}")