def bubble_sort_positive(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Пропускаем сравнение, если элемент отрицательный или уже отсортирован
            if arr[j] <= 0 or arr[j+1] <= 0:
                continue
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def comb_sort_positive(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            # Пропускаем сравнение, если элемент отрицательный или уже отсортирован
            if arr[i] <= 0 or arr[i+gap] <= 0:
                i += 1
                continue
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                sorted = False
            i += 1

    return arr

# Пример использования
array = [6, 5, 3, 1, 2, -5, 7, -3, 8]
print("Исходный массив:", array)

# Сортировка пузырьком
sorted_array_bubble = bubble_sort_positive(array.copy())
print("Отсортированный массив (пузырьковая сортировка):", sorted_array_bubble)

# Сортировка расческой
sorted_array_comb = comb_sort_positive(array.copy())
print("Отсортированный массив (расческая сортировка):", sorted_array_comb)

"""
7.Отсортировать положительные элементы одномерного массива, отрицательные оставить на местах.
Сортировки: пузырьковая и расческой.
"""