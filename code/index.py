def persegi_panjang():
    width = int(input("Masukkan lebar : "))
    height = int(input("Masukkan panjang : "))

    hasil = width * height

    print(f'persegi panjang dengan panjang {height} dan lebar {width} memiliki luas {hasil}')



def bola():
    jari = float(input("Masukkan jari - jari : "))

    hasil = 4/3 * 22/7 * jari**3 if jari % 7 == 0 else 4/3 * 3.14 * jari**3

    print(f'bola dengan jari - jari {jari} memiliki volume {hasil}')



def texto():
    texto = input("Masukkan texto pertama : ")
    texto_2 = input("Masukkan texto kedua : ")
    texto_3 = input("Masukkan texto ketiga : ")

    print(f'{texto} {texto_2} {texto_3}')



def absensi():
    sick = input("Apakah siswa sakit? ")

    if sick in ['yes', 'y', 'ya', 'true']:
        print('Siswa tidak bisa mengikuti pembelajaran')
    else:
        print('Siswa bisa mengikuti pembelajaran')



persegi_panjang()
bola()
texto()
absensi()