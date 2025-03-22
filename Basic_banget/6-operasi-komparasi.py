# Operasi Komparasi

# >,<,>=,<=, ==, !=, is, is not

a = 3
b = 6

print(f"\nLebih Dari")
hasil = a > 3
print(f"a > 3 = {hasil}")
hasil = b > 3
print(f"b > 3 = {hasil}")
hasil = b > 6
print(f"b > 6 = {hasil}")

print(f"\nKurang Dari")
hasil = a < 3
print(f"a < 3 = {hasil}")
hasil = b < 3
print(f"b < 3 = {hasil}")
hasil = b < 6
print(f"b < 6 = {hasil}")

print(f"\nLebih Dari Sama Dengan")
hasil = a >= 3
print(f"a >= 3 = {hasil}")
hasil = b >= 3
print(f"b >= 3 = {hasil}")
hasil = b >= 6
print(f"b >= 6 = {hasil}")

print(f"\nKurang Dari Sama Dengan")
hasil = a <= 3
print(f"a <= 3 = {hasil}")
hasil = b <= 3
print(f"b <= 3 = {hasil}")
hasil = b <= 6
print(f"b <= 6 = {hasil}")

print(f"\nSama Dengan")
hasil = a == 3
print(f"a == 3 = {hasil}")
hasil = b == 3
print(f"b == 3 = {hasil}")
hasil = b == 6
print(f"b == 6 = {hasil}")

print(f"\nTidak Sama Dengan")
hasil = a != 3
print(f"a != 3 = {hasil}")
hasil = b != 3
print(f"b != 3 = {hasil}")
hasil = b != 6
print(f"b != 6 = {hasil}")

print(f"\nObject identity (is)")
hasil = a is b
print(f"a is b = {hasil}")

print(f"\nObejct identity (is not)")
hasil = a is not b
print(f"a is not b = {hasil}")
