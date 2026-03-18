def bubbleSort(array):
    swapped = 0
    for i in range(number):
        print(f'current iteration is {i + 1}')
        for j in range(0, number - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped += 1
                print(f'modified array is {array}')
        if swapped == 0:
            break
    print(50 * '-')
    print(f'number of swaps is {swapped}')
    return array

number = int(input('number of array elements: '))
array = []      
for i in range(number):
    element = int(input(f'enter the element {i + 1}:'))
    array.append(element)
print(50 * '-')
result = bubbleSort(array)
print(f'sorted array is {result}')
print(50 * '-')