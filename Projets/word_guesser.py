life = 7
guess = "Hello"
user = "_" * len(guess)
guess_word = guess.lower()
user_word = user.lower()

while life and guess_word != user_word:
    letter = input("Entrz une lettre ")
    if letter in guess_word:
        for i in range(len(guess_word)):
            if guess_word[i] == letter:
                user_word = user_word[:i] + letter + user_word[i + 1:]

            
    if guess_word == user_word:
        print("Bravo ta mere, le mot est : ", guess_word)
        break
    else:
        print("Votre vie est : ", life)
        print("Votre mot est : ", user_word)
        life -= 1

        