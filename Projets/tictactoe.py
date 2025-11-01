from tictactoe_robot import get_turn

empty = " "
dashboard = [empty for i in range(9)]
current_player = "X"
emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

def show_dashboard():
    print("-" * 13)
    for i in range(9):
        print("|", dashboard[i] if dashboard[i] != empty else emojis[i], end=" ")
        if i % 3 == 2:
            print("|")
            print("-" * 13)
    print("")

print("")
print("Bienvenue dans le jeu TicTacToe !")
print("")

while True:
    show_dashboard()
    player_choice = 0

    if current_player == "O":
        player_choice = get_turn(dashboard) + 1


    try:
        print("Choisissez la case voulue")

        if current_player == "X":
            player_choice = int(input(f"Joueur {current_player} : "))

        if player_choice > 9 or player_choice < 1:
            print("Vous devez choisir une valeur entre 1 et 9 ")
            continue

        elif dashboard[player_choice - 1] != empty:
            print("La case choisie est déjà prise ")
            continue

        else:
            dashboard[player_choice - 1] = current_player
            if current_player == "O":
                print(f"Le bot à jouer à la case {player_choice}")
            else:
                print(f"Vous avez jouez à la case {player_choice}")

            if all(cell != empty for cell in dashboard):
                show_dashboard()
                print("Match nul !")
                break

            if empty != dashboard[0] == dashboard[1] == dashboard[2] \
            or empty != dashboard[3] == dashboard[4] == dashboard[5] \
            or empty != dashboard[6] == dashboard[7] == dashboard[8] \
            or empty != dashboard[0] == dashboard[3] == dashboard[6] \
            or empty != dashboard[1] == dashboard[4] == dashboard[7] \
            or empty != dashboard[2] == dashboard[5] == dashboard[8] \
            or empty != dashboard[2] == dashboard[4] == dashboard[6] \
            or empty != dashboard[0] == dashboard[4] == dashboard[8]:
                show_dashboard()
                print(f" 🎉🎉🎉 Le joueur {current_player} gagne la partie")
                
                choice = input("Voulez vous une autre partie ? Oui(O) ou Non(N) ")
                if choice == "O":
                    dashboard = [empty for _ in range(9)]
                    continue
                elif choice == "N":
                    break
                else:
                    print("Entrez Oui ou Non")

            current_player = "O" if current_player == "X" else "X"
            continue
    except:
        print("Veuillez entrez une valeur correcte ")

