import random

random_num = random.randint(0, 10)
life = 2


while life >= 0:
    user_num = input("Entrez le chiffre ")
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num > random_num:
            life -= 1
            print(f"C'est plus bas ⬇️ attention vous avez {life} chances restants")
        elif user_num < random_num:
            life -= 1
            print(f"C'est plus haut ⬆️ attention vous avez {life} chances restants")
        else:
            print(f"Bravo vous avez trouvé le bon chiffre c'était bien {random_num}")
            break
    else:
        print("Entrez un chiffre uniquement svp ")
    
    if life == 0:
        print(f"Vous avez perdu le bon chiffre était {random_num}")
    