# num = input("Enter a number :")
# sum = 0
# # addition = sum(int(ch)**len(num) for ch in num)
# for i in num:
#     sum += int(i) ** len(num)
# num = int(num)
# if num == sum:
#     print(f"The number {num} is armstrong number")
# else:
#     print(f"The number {num} is not an armstrong number")
lst = []

for i in range(1, 5000):
    s = str(i)
    power = len(s)
    total = 0
    for digit in s:
        total += int(digit) ** power
    if total == i:
        lst.append(i)
print(lst)

total_sum = str(sum(lst))
print(f"the sum of all armstrong numbers from 1 to 5000 is {sum(lst)}")

temp = str(total_sum)

while len(temp) > 1:
    digit_sum = 0
    for digit in temp:
        digit_sum += int(digit)
    print(digit_sum)
    temp = str(digit_sum)
