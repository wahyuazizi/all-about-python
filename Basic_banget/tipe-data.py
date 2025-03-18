"""
    Belajar tipe data python
"""

# Brupa text
def dtype_str():
    """
    str adalah tipe data berupa string, seperti huruf abjad atau simbol lain
    """
    namaku = "ilustraziz"
    emailku = "ilustraziz@contoh.com"

    print(namaku)
    print(emailku)

# Berupa angka
def dtype_int():

    bulan = 3
    tahun_lahir = 2004

    print(bulan)
    print(tahun_lahir)

def dtype_float():
    nilaku = 86.2
    nilai_teman = 20.3423

    print(nilaku)
    print(nilai_teman)

def dtype_complex():
    x_complex = complex(2.3)
    y_complex = complex(2j)

    print(x_complex)
    print(y_complex)

# Berupa urutan
def ini_list():
    nama = ["budi", "zoro", "luffy"]
    nilai = [89, 15, 5]

    print(nama)
    print(nilai)

def ini_tuple():
    nama = ("budi", "zoro", "luffy")
    nilai = (12, 13, 14)

    print(nama)
    print(nilai)

def ini_set():
    nama = {"budi", "zoro", "luffy"}
    nilai = {12, 13, 14}

    print(nama)
    print(nilai)

def ini_frozenset():
    nama = frozenset(["budi", "zoro", "luffy"])
    nilai = frozenset([12,13,14])

    print(nama)
    print(nilai)

# Berupa map
def ini_dict():
    hari={
        "sen": "senin",
        "sel": "selasa",
        "rab": "rabu"
    }

    print(hari)

# Berupa data binary
def ini_bytes():
    angkaku = bytes(12)
    angkaku_1 = bytes(245)

    print(angkaku)
    print(angkaku_1)

def ini_bytearray():
    angkaku = bytearray(12)
    print(angkaku)

def ini_memoyview():
    angka_saya = memoryview(bytes(12))
    angka_saya1 = memoryview(bytes(1212))
    print(angka_saya)
    print(angka_saya1)



if __name__=="__main__":

    tipe_str = dtype_str()
    tipe_str

    print("=="*5, "integer", "=="*5)

    tipe_int = dtype_int()
    tipe_int

    print("=="*5, "float", "=="*5)

    tipe_float = dtype_float()
    tipe_float

    print("=="*5, "complex", "=="*5)

    tipe_cmplx = dtype_complex()
    tipe_cmplx

    print("=="*5, "list", "=="*5)

    tipe_list = ini_list()
    tipe_list

    print("=="*5, "tuple", "=="*5)

    tipe_tuple = ini_tuple()
    tipe_tuple

    print("=="*5, "set", "=="*5)

    tipe_set = ini_set()
    tipe_set

    print("=="*5, "frozenset", "=="*5)

    tipe_frozenset = ini_frozenset()
    tipe_frozenset

    print("=="*5, "dict", "=="*5)

    tipe_dict = ini_dict()
    tipe_dict

    print("=="*5, "bytes", "=="*5)

    tipe_bytes = ini_bytes()
    tipe_bytes

    print("=="*5, "bytearray", "=="*5)

    tipe_bytearray = ini_bytearray()
    tipe_bytearray

    print("=="*5, "bytes", "=="*5)

    tipe_memoryview = ini_memoyview()
    tipe_memoryview