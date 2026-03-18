def bubbleSortCount(arr):
    print(f'Input array {arr}')
    n = len(arr)
    swap_count = 0

    for i in range(n):
        print(f'\nPass {i+1}')
        for j in range(0, n - i - 1):
            print(f'Comparing {arr[j]} and {arr[j+1]}')

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1

            print(f'Array now: {arr}')

    print("Total swaps:", swap_count)

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSortCount(arr)
print("Sorted array:", arr)