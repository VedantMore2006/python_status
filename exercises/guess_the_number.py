import random


def guess_the_num():
    print("The number is within and including both 0 and 100")
    while True:
        a = random.randint(0, 100)
        while True:
            guess = int(input("Guess the number : "))
            if guess > a:
                print("The Guess is greater. Try a smaller number.")
            elif guess < a:
                print("The Guess is smaller. Try a greater number.")
            else:
                print(f"The number {guess} is Correct guess")
                break
        again = input(
            "Wanna give a try again!!\nType 'y' for yes and 'n' for no : "
        ).lower()
        if again == "n":
            break


guess_the_num()
