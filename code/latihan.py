# def str_to_bool(s):
#     return s.lower() in ['true', 't', '1', 'yes','y']
#
# sakit = str_to_bool(input("Sakit? "))
#
# if sakit:
#     print("mahasiswa ijin tidak hadir kuliah")
# else:
#     print("mahasiswa tidak ditemukan")


# def latihan_3():
#     a = 6
#     return a
#
# def latihan_4():
#     print(5 + latihan_3())
#
# latihan_3()
# latihan_4()

# nilai = int(input("Nilai: "))
#
# if nilai >= 85:
#     print("A")
# elif nilai >=70:
#     print("B")
# elif nilai >=55:
#     print("C")
# elif nilai >=40:
#     print("D")
# else:
#     print("E")

# biaya = int(input("Biaya:"))
# jarak = int(input("Jarak:"))
# fasilitas = input("Fasilitas:").lower()
#
# if biaya <1000000:
#     if jarak <=3:
#         if fasilitas=="lengkap": print("Sangat direkomendasikan")
#     elif jarak <=5:
#         if fasilitas=="lengkap": print("Direkomendasikan")
# elif biaya <=2000000:
#     if jarak <=5:
#         if fasilitas=="lengkap": print("Direkomendasikan")
#         else:
#             print("Kurang direkomendasikan")
#     elif jarak >5:
#         if fasilitas=="lengkap": print("Kurang direkomendasikan")
#         else:
#             print("Tidak direkomendasikan")
# else:
#     print("Tidak direkomendasikan")

nilai = input("Nilai:").upper ()
match nilai:
    case "A":
        print("Akreditasi Unggul")
    case "B":
        print("Akreditasi Baik Sekali")
    case "C":
        print("Akreditasi Baik")
    case _:
        print("Tidak terakreditasi")