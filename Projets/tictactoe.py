empty = " "
dashboard = [empty for i in range(9)]
current_player = "X"
player_choice = 0
emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

def show_dashboard():
    for i in range(9):
        print(dashboard[i], end=" ")
        if i % 3 == 2:
            print("")

while True:
    show_dashboard()
    try:
        player_choice = int(input(f"Joueur {current_player} "))
        if player_choice > 9 or player_choice < 1:
            print("Vous devez choisir une valeur entre 1 et 9 ")
            continue
        elif dashboard[player_choice - 1] != empty:
            print("La case choisie est déjà prise ")
            continue
        else:
            dashboard[player_choice - 1] = current_player

            if empty != dashboard[0] == dashboard[1] == dashboard[2] \
            or empty != dashboard[3] == dashboard[4] == dashboard[5] \
            or empty != dashboard[6] == dashboard[7] == dashboard[8] \
            or empty != dashboard[0] == dashboard[3] == dashboard[6] \
            or empty != dashboard[1] == dashboard[4] == dashboard[7] \
            or empty != dashboard[2] == dashboard[5] == dashboard[8] \
            or empty != dashboard[2] == dashboard[4] == dashboard[6] \
            or empty != dashboard[0] == dashboard[4] == dashboard[8]:
                print(f"Le joueur {current_player} gagne la partie")
                break

            current_player = "O" if current_player == "X" else "X"
            continue
    except:
        print("Veuillez entrez une valeur correcte ")

