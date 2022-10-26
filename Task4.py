# Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.

array =[1, 5, 2, 3, 4, 6, 1, 7]

def ascending_sequence(array):
    final_array = []
    temporery_array = []
    j = 1

    while j < len(array):
        i = j
        copy_array = array[:]
        while i < len(copy_array) - 1:
            if copy_array[i] < copy_array[i+1]:
                temporery_array.append(copy_array[i])
                i += 1
            else:
                copy_array.pop(i+1)
        j += 1
        if len(final_array) < len(temporery_array):
            final_array = temporery_array
        temporery_array = []
    if array[-1] > final_array[-1]:
        final_array.append(array[-1])
    if array[0] < final_array[0]:
        final_array.insert(0, array[0])

    return final_array


print(ascending_sequence(array))                            