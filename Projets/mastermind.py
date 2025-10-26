import random
life = 10
lenght = 5
colors_letter = ["R", "V", "B", "N", "J", "M", "O"]
colors_name = ["Rouge", "Vert", "Bleu", "Noir", "Jaune", "Marron", "Ornage"]
colors_emoji = {'R': '🔴', 'V': '🟢', 'B': '🔵', 'N': "⚫️", 'J': '🟡', 'M': "🟤" ,'O': '🟠'}
guess_colors = random.choices(colors_letter, k=lenght)
colors = "".join(colors_emoji[color] for color in guess_colors)


def enter():
    while True:
        user_guess = input(f"Entrez la combinaison de {lenght} couleurs (ex: RVBNO) ").upper().replace(" ", "")
        if len(user_guess) != lenght:
            print(f"Vous devez entrez {lenght} couleurs. Réessayez")
            continue

        if all(c in colors_letter for c in user_guess):
            return list(user_guess)
        else: 
            print("Seuls ces combinaisons sont disponible : " + " ".join(colors_letter))

def feedback(random, enter):
    good = 0
    wrong = 0
    random_temp = random[:]
    enter_temp = enter[:]

    for i in range(lenght):
        if enter[i] == random[i]:
            good += 1
            random_temp[i] = enter_temp[i] = None

    for c in enter_temp:
        if c and c in random_temp:
            wrong += 1
            random_temp[random_temp.index(c)] = None

    return good, wrong

def dashboard(data):
    print("\n" + "="*40)
    print("📊 PLATEAU DE JEU ")
    print("="*40)
    for i, (essai, good, wrong) in enumerate(data, 1):
        emojis = "".join(colors_emoji[color] for color in essai)
        indices = "●" * good + "○" * wrong
        print(f"{i:2d}. {emojis} | {indices}")
    print("="*40)


history = []
print(f"Devinez la séquence de {lenght} couleurs")
print("Couleurs disponibles : ")
for i in range(len(colors_letter)):
    print(f"{colors_emoji[colors_letter[i]]} {colors_letter[i]} = {colors_name[i]}")

for i in range(life):
    print(f"Vous avez {life - i} essai(s)")
    essai = enter()

    good, wrong = feedback(guess_colors, essai)
    print(f"✅ Bien placée(s) : {good} | ⚠️ Mal placée(s) {wrong}")

    history.append((essai, good, wrong))
    dashboard(history)

    if good == lenght:
        print(f"🎉 Bravo vous avez trouvé la combinaison ! {colors}")
        break
else:
    print(f"Vous avez perdu la combinaison était : {colors}")
