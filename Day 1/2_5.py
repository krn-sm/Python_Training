def duplicate(arr):
    new_arr = []
    for i in range(0, len(arr)-1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
              new_arr.append(arr[i])
    return new_arr
arr = list(map(int, input("Enter the elements: ").split(" ")))
print("The duplicate numbers are ")
new_arr = duplicate(arr)
for i in new_arr:
    print(i, end=' ')