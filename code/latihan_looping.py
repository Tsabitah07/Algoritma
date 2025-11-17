def average():
    score_sum = input(f'Masukkan banyak data: ')
    scores = []

    for index in range(int(score_sum)):
        score = input(f'Masukkan nilai {index + 1}: ')
        scores.append(int(score))

    avg = sum(scores) / len(scores)
    print(f'Rata - rata nilainya adalah {avg}')



def odd_numbers():
    max_num = int(input(f'Masukkan nilai maximum: '))
    numbers = []
    numbers_2 = []
    for index in range(max_num + 1):
        if index % 2 == 0:
            numbers.append(index)
        else:
            numbers_2.append(index)

    odd_num_sum = sum(numbers)
    print(f'Angka Genap {numbers}')
    print(f'Angka Ganjil {numbers_2}')
    print(f'Jumlah angka genap diantara 1 - {max_num} adalah {odd_num_sum}')



average()
odd_numbers()