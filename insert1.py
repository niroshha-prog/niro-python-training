def InsertionSort(arr):
    n = len(arr)
    
    if n <= 1:
        return
        
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

user_input = input("Enter words separated by space: ")
words = user_input.split()

InsertionSort(words)

print(words)