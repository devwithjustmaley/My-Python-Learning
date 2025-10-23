import random

def score(u1, u2):
    print(f"Joueur : {u1} / Robot : {u2}")

def game(u1, u2):
    global player_points, robot_points, series
    if (u1 == "F" and u2 == "P") or (u1 == "P" and u2 == "C") or (u1 == "C" and u2 == "F"):
        print("le JOUEUR GAGNE")
        player_points += 1
        score(player_points, robot_points)
        series -= 1
    if (u2 == "F" and u1 == "P") or (u2 == "P" and u1 == "C") or (u2 == "C" and u1 == "F"):
        print("le ROBOT GAGNE")
        robot_points += 1
        score(player_points, robot_points)
        series -= 1
    if u1 == u2:
        print("Manche nulle")
        score(player_points, robot_points)



robot_points = 0
player_points = 0
series = input("Combien de manches voulez vous ? ")
series = int(series)
elements = ["P", "F", "C"]

print(type(series))

while series > 0:
    number = random.randint(0, 2)
    robot_game = elements[number]
    user_game = input("Choisissez entre Pierre(P), Papier(F), Ciseaux(C) ")
    game(user_game, robot_game)
