# 2. WAP which keeps prompting user to guess a word. The user is allowed up
# to 10 guesses. Write your code in such a way that the secret word and the
# number of allowed guesses are easy to change. Print messages to give the
# user feedback.

guess = None
word = "Noodles"
TotalGuess = 5
guess_left = TotalGuess

while guess != word and guess_left > 0:
    guess = input("Enter word guess: ")
    if guess == word:
        print("Correct guess!")
        break
    else:
        guess_left = guess_left - 1
        if guess_left != 0:
            print("Incorrect, try again")
        else:
            print("Incorrect, you lose")
