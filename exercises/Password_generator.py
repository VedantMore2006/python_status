import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letter = int(input("No of letters in the password : "))
nr_symbols = int(input("No of Symbols in the password : "))
nr_numbers = int(input("No of numbers in the password : "))
password = []
for n in range(0, nr_letter):
    password += random.choice(letters)
for n in range(0, nr_symbols):
    password += random.choice(symbols)
for n in range(0, nr_numbers):
    password += random.choice(numbers)

print(f"Combined password or rather the Combined string {password}")
random.shuffle(password)
print(f"Shuffled password string is : {password}")
passwordn = ""
for char in password:
    passwordn += char
print(f"Your password is {passwordn}")
