##Q1. Find the maximum element in its index in an array. 
arr = [25, 26, 56, 90, 38]
max = 0
index = 0
max_index = None
for i in arr:
    index += 1
    if max < i:
        max = i
        max_index = index - 1

if arr[max_index] == max:
    print(f"The max number in the list is {max} and its index is {max_index}")