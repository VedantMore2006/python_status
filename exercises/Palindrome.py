def palindrome(n):
    while n != str(n)[::-1]:
        print(n)
        n += str(n)[::-1]
    return n


num = input("Number : ")
if num == str(num)[::-1]:
    print("Number is already palindrome")
else:
    print(f"the plaindrome is {palindrome(num)}")
