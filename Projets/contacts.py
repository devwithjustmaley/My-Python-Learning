FILENAME = "contacts.txt"

def show_contacts(data):
    if not data:
        print("Aucun résultat trouvé")
        return
    
    print(f"\nVos {len(data)} contacts : ")
    for i, (name, phone) in enumerate(data, 1):
        print(f"{i} - {name} : {phone}")

def get_contacts():
    contacts = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, phone = line.split(";")
                    contacts.append([name, phone])
            print(f"\n{len(contacts)} contacts chargés")
    except FileNotFoundError:
        print("Pas de fichier trouvé")
    return contacts

def add_contacts(data):
    print("\nAjouter un contact : ")
    while True: 
        name = input("Nom : ").strip()
        phone = input("Numéro de téléphone : ").strip()
        if name and phone:
            if len(phone) < 10:
                print("Numéro de téléphone invalide")
                continue
            data.append([name, phone])
            print(f"{name} ajouté à vos contacts avec succès")
            break
        else:
            print("Nom et numéro de téléphone obligatoire pour ajouter un contact")

def save_contact(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for name, phone in data:
            file.write(f"{name};{phone}\n")
        print("Les contacts ont été mise à jour")

def remove_contact(data):
    name = input("\nNom du contact à supprimer: ").strip()
    new = [c for c in data if name not in c[0]]
    if len(new) == len(data):
        print(f"Aucun contact trouvé pour {name}")
    else:
        save_contact(new)
        data[:] = new
        print(f"{name} à bien été supprimé de vos contacts")


def menu():
    print("=== GESTIONNAIRE DE CONTACTS ===")

    contacts = get_contacts()

    while True:
        print("\n Que voulez vous faire ?")
        print("1. Voir les contacts")
        print("2. Ajouter un contact")
        print("3. Supprimer un contact")
        print("4. Sauvegarder et quitter le programme")

        choice = input("=> ")

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            save_contact(contacts)
            print("Au revoir")
            break
        else:
            print("Choix invalide")
    
menu()
