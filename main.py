from PIL import Image
import numpy as np

def hash(image, size):
    new = image.resize((size, size))
    new = new.convert('L')
    arr = np.array(new)
    avr = arr.sum()

    # вычисляем среднее значение пикселя
    avr = avr / arr.size

    # изменяем значения в матрице картинки. Если оно больше порога - присваиваем значение 255, иначе - 0
    arr[arr < avr] = 0
    arr[arr > avr] = 255
    binarization_arr = np.ndarray.copy(arr) # копируем матрицу для последующей отрисовки в картинку

    arr[arr == 255] = 1 # заменяем 255 на 1 для корректной работы алгоритма перевода в 16-ое число
    ones_matrix = np.ndarray.copy(arr) # копия матрицы единиц для нахождения расстояния Хэмминга
    ones_matrix = ones_matrix.astype(np.int8) # для корректной операции вычитания матриц друг из друга

    arr = np.reshape(arr, size*size)
    arr = arr.astype(np.int8)
    arr = arr[::-1]
    arr = np.nonzero(arr)[0]
    res = 0
    for i in arr:
        res += 2**i
    res = hex(res)

    return binarization_arr, res, ones_matrix

image = Image.open('cat.jpg')
array1, res1, arr_ones = hash(image, 8)
print(array1)
print(res1)
image2 = Image.open('cat2.jpg')
array2, res2, arr_ones2 = hash(image2, 8)
print(array2)
print(res2)

hamming_ditance = arr_ones2 - arr_ones
non = np.nonzero(hamming_ditance)
match_percent = 100 - (non[0].size / array1.size * 100)
print(match_percent, "% совпадения между сравниваемыми изображениями")
print(non[0].size, "- расстояние Хэмминга в сравниваемых изображениях")


# вывод бинаризированных изображений размером size x size
last = Image.fromarray(array1).convert('L')
last.show()
last = Image.fromarray(array2).convert('L')
last.show()