caracteres = {
    1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
    10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R",
    19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z",
    27: "a", 28: "b", 29: "c", 30: "d", 31: "e", 32: "f", 33: "g", 34: "h", 35: "i",
    36: "j", 37: "k", 38: "l", 39: "m", 40: "n", 41: "o", 42: "p", 43: "q", 44: "r",
    45: "s", 46: "t", 47: "u", 48: "v", 49: "w", 50: "x", 51: "y", 52: "z",
    53: "à", 54: "â", 55: "ä", 56: "é", 57: "è", 58: "ê", 59: "ë", 60: "î", 61: "ï",
    62: "ô", 63: "œ", 64: "ù", 65: "û", 66: "ü", 67: "ç",
    68: "!", 69: "?",
    70: ",", 71: ".", 72: ";", 73: ":", 74: '"', 75: "'",
    76: "0", 77: "1", 78: "2", 79: "3", 80: "4", 81: "5", 82: "6", 83: "7", 84: "8", 85: "9",
    86: " "
}

texto_encriptado = input("Saisissez le texte crypté :")

numeros = []
for numero_encriptado in texto_encriptado.split():
    numero = (int(numero_encriptado) - 2) // 2
    if numero in caracteres:
        numeros.append(numero)

texto_descifrado = "".join(caracteres[numero] for numero in numeros)
print(texto_descifrado)