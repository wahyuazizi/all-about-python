"""
    Merubah dari satu ke tipe lain
"""
# INTEGER
print("=="*5, "INTEGER", "=="*5)
data_int = 9
print("data = ", data_int, ", type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # Akan false jika nilai int =0
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

# FLOAT
print("=="*5, "FLOAT", "=="*5)
data_float = 9.5
print("data = ", data_float, ", type =", type(data_float))

data_int = int(data_float) # dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # Akan false jika nilai float =0
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

# BOOL
print("=="*5, "BOOLEAN", "=="*5)
data_bool = True
print("data = ", data_bool, ", type =", type(data_bool))

data_int = int(data_bool) # dibulatkan kebawah
data_str = str(data_bool)
data_float = float(data_bool) # Akan false jika nilai float =0
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_float, ", type =", type(data_float))


# STRING
print("=="*5, "STRING", "=="*5)
data_str = "10" 
print("data = ", data_str, ", type =", type(data_str))

data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # kalau str kosong akan bernilai true
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_bool, ", type =", type(data_bool))
