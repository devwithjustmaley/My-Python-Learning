def fibonacci(n):
    a, b = 0, 1
    array = []
    for _ in range(n):
        array.append(a)
        a, b = b, a + b
    return array

while True:
    nb = input("Entre le nombre de terme que vous voulez ")
    if nb.isdigit():
        if int(nb) > 0:
            break
    else:
        print("Entrez un chiffre correct")
        continue

print(f"Les {nb} premiers termes de la suite de Fibonnaci sont : {fibonacci(int(nb))}")