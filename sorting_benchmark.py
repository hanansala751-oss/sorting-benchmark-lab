import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = []
    mid = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            mid.append(x)
        else:
            right.append(x)
    return quick_sort(left) + mid + quick_sort(right)

def make_data(n, typ):
    if typ == "sorted":
        return list(range(n))
    if typ == "reversed":
        return list(range(n, 0, -1))
    return [random.randint(0, n*10) for _ in range(n)]

def test_time(func, data):
    d = data[:]
    s = time.perf_counter()
    func(d)
    e = time.perf_counter()
    return e - s

sizes = [100, 1000, 10000, 100000]
types = ["sorted", "reversed", "random"]

funcs = {
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "python_sorted": sorted
}

for t in types:
    plt.figure()
    for name, f in funcs.items():
        times = []
        for n in sizes:
            data = make_data(n, t)
            if name == "insertion" and n == 100000:
                times.append(0)
                continue
            tm = test_time(f, data)
            times.append(tm)
        plt.plot(sizes, times, marker='o', label=name)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('n')
    plt.ylabel('time (s)')
    plt.title(f'benchmark - {t}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{t}.png')
    plt.show()