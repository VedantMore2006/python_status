arr = [7, 3, 2, 5, 1, 9]
index = 0
min = 10 #The reason why I have taken here min equals to 10 because if I were to take this 0 the condition wouldn't be satisfied of that if your i is greater than min and whatever the value will be within the minimum variable or min variable that will only be carried forward and the output will only be 0 but now that I have given it a greater  value so it literally compares with the i that is in our list of this name air so 
         #that is the reason.
min_index = None
for i in arr:
    index += 1
    if i < min:
        min = i
        min_index = index - 1
print("the minimum element is", min, "and its index is", min_index)