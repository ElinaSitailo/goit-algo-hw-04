# Python має дві вбудовані функції сортування: sorted і sort.
# Функції сортування Python використовують Timsort - гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.
# Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання.
# Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних.
# Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах.
# Для заміру часу виконання алгоритмів використовуйте модуль timeit.

# Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим,
# і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі.
# Зробіть висновки.
import random
import timeit
import copy


def merge_sort(arr):
    """Сортування злиттям"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def insertion_sort(arr):
    """Сортування вставками"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def test_sorting_algorithms(sizes):
    """Тестування та вимірювання часу виконання алгоритмів сортування"""
    merge_sort_times = []
    insertion_sort_times = []
    timsort_times = []

    for size in sizes:
        print(f"Тестування масиву розміром: {size}...")
        data = [random.randint(0, 10000) for _ in range(size)]

        data_copy = copy.deepcopy(data)
        merge_time = timeit.timeit(lambda: merge_sort(data_copy), number=1)
        merge_sort_times.append(merge_time)

        data_copy = copy.deepcopy(data)
        insertion_time = timeit.timeit(lambda: insertion_sort(data_copy), number=1)
        insertion_sort_times.append(insertion_time)

        data_copy = copy.deepcopy(data)
        timsort_time = timeit.timeit(lambda: sorted(data_copy), number=1)
        timsort_times.append(timsort_time)

    return merge_sort_times, insertion_sort_times, timsort_times


array_sizes = [10, 100, 500, 1000, 5000, 10000, 20000, 50000, 100000]
print(f"Старт тестування алгоритмів сортування на масивах чисел: {array_sizes}")

merge_times, insertion_times, ptimsort_times = test_sorting_algorithms(array_sizes)

print(
    f"{'Size':<10}{'Merge Sort (s)':<20}{'Insertion Sort (s)':<20}{'Timsort (s)':<20}"
)
for i in range(len(array_sizes)):
    print(
        f"{array_sizes[i]:<10}{merge_sort_times[i]:<20.6f}{insertion_sort_times[i]:<20.6f}{timsort_times[i]:<20.6f}"
    )
# Висновки
print("\nВисновки:")
print("1. Сортування вставками є ефективним тільки для малих наборів даних.")
print(
    "2. Сортування злиттям має кращу продуктивність на більших наборах даних, але поступається Timsort."
)
print("3. Timsort демонструє найкращу продуктивність на всіх розмірах даних.")
