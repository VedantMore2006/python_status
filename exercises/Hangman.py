import random

stage = [1, 2, 3, 4, 5, 6]
print(stage[1])
word_list = ["already", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in chosen_word:
    display += "-"
print(display)
guess = ""
lives = 6
end = False
while not end and lives > 0:
    guess = input("Guess a letter : ")
    for n in range(0, len(chosen_word)):
        if guess == chosen_word[n]:
            display[n] = guess
    print(display)
    if guess not in chosen_word:
        lives -= 1
    elif "-" not in display:
        end = True
        print("won")
if lives == 0:
    print("you lose")
# for n in chosen_word:
#     if guess == n:
#         print("Right")
#     else:
#         print("Wrong")
#
