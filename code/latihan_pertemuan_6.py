# #1. Arithmetics Series
def excercise_1():
    def arithmetics_series(a, b, n):
        if n == 0:
            return []
        return arithmetics_series(a, b, n - 1) + [a + (n - 1) * b]

    a = int(input("Masukkan nilai suku pertama [a] : "))
    b = int(input("Masukkan nilai selisih [b] : "))
    n = int(input("Masukkan banyak suku [n] : "))

    print(arithmetics_series(a, b, n))


# #2. Print Stars
def excercise_2():
    def stars(n):
        if n == 0:
            return ""
        else:
            print('*', end='')
            return stars(n - 1)

    star = int(input("Masukkan banyak bintang : "))
    print(stars(star))


#3. Fibbonacci Series
def excercise_3():
    def fibbonacci_series(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib = fibbonacci_series(n - 1)
            fib.append(fib[-1] + fib[-2])

            return fib

    def fibbonacci_nth(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibbonacci_nth(n-1) + fibbonacci_nth(n-2)

    def fibbonacci_sum(n):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibbonacci_nth(n) + fibbonacci_nth(n-1)

    fib_input = int(input("Masukkan banyak suku fibbonacci: "))
    print(f'Deret Fibbonacci = {fibbonacci_series(fib_input)}')
    print(f'Jumlah dari fibbonacci n = {fib_input} adalah {fibbonacci_sum(fib_input)}')


#4. Combination
def excercise_4():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    def combination(n, r):
        if r > n:
            return 'r tidak boleh lebih besar dari n'
        elif r == 0 or r == n:
            return 1
        else:
            return factorial(n) // (factorial(r) * factorial(n - r))

    n = int(input("Masukkan nilai n : "))
    r = int(input("Masukkan nilai r : "))

    print(f'Kombinasi dari n = {n} dan r = {r} adalah {combination(n, r)}')



excercise_1()
excercise_2()
excercise_3()
excercise_4()