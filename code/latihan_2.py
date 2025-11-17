def task_1():
    angka = int(input("angka = "))

    if angka % 5 == 0:
        print(f'angka {angka} merupakan kelipatan 5')
    else:
        print(f'angka {angka} bukan merupakan kelipatan 5')



def task_2():
    angka = int(input("masukkan sudut = "))

    if angka <90:
        print(f'angka {angka} merupakan sudut lancip')
    elif angka == 90:
        print(f'angka {angka} merupakan sudut siku - siku')
    elif angka <= 180:
        print(f'angka {angka} merupakan sudut tumpul')
    else:
        print(f'angka {angka} bukan sudut segitiga')



def task_3():
    print("Tentukan jenis akar persamaan kuadrat Ax2 + Bx + C = 0")
    a = input("masukkan A = ")
    b = input("masukkan B = ")
    c = input("masukkan C = ")

    d = b ** 2 - 4 * a * c

    if d > 0:
        print("Jenisnya adalah Akar Riil Berbeda")
    elif d == 0:
        print("Jenisnya adalah Akar Riil Sama")
    else:
        print("Jenisnya adalah Akar Imajiner")




def task_4():
    semester = int(input("masukkan semester = "))
    ipk = float(input("masukkan ipk = "))
    ielts = float(input("masukkan ielts = "))

    if semester >= 4 and ipk >= 3.0 and ielts >= 5.5:
        print(f'Anda memenuhi syarat')
    else:
        print(f'Anda tidak memenuhi syarat')



task_1()
task_2()
task_3()
task_4()