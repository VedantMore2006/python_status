num = input("Enter a number :")
sum = 0
# addition = sum(int(ch)**len(num) for ch in num)
for i in num:
    sum += int(i) ** len(num)
num = int(num)
if num == sum:
    print(f"The number {num} is armstrong number")
else:
    print(f"The number {num} is not an armstrong number")
