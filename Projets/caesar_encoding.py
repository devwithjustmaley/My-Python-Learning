def chifer(msg, shift=3, decode=False):

    if decode:
        shift = -shift

    result = ""
    
    for letter in msg.upper():
        if letter.isalpha():
            ascii_value = ord(letter) - ord("A")
            shifted = (ascii_value + shift) % 26
            result += chr(shifted + ord("A"))
        else:
            result += letter
    
    return result


encoded = chifer(input("Entrez le message à chiffrer "))
decoded = chifer(encoded, decode=True)
print(f"Chiffré : {encoded} Non chiffré : {decoded}")