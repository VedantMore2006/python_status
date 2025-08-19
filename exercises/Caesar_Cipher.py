def encrypt(etext, eshift):
    cipher_text = ""
    for i in etext:
        position = alphabets.index(i)
        cipher_text += alphabets[position + eshift]
    print(cipher_text)


def decrypt(cipher_text, dshift):
    decrypt_text = ""
    for i in cipher_text:
        position = alphabets.index(i)
        decrypt_text += alphabets[position - dshift]
    print(decrypt_text)


again = 0
while again != 1:
    alphabets = [
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
    ]
    direction = input("Type encode to encrypt : \nType decode to decrypt : \n -> ")
    text = input("Type your message : ")
    shift = int(input("Type the shift number : "))

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    again = int(input("If u want to do it again type '0' or '1' to exit : "))
