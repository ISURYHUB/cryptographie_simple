caracteres = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
    "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
    "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26,
    "a": 27, "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35,
    "j": 36, "k": 37, "l": 38, "m": 39, "n": 40, "o": 41, "p": 42, "q": 43, "r": 44,
    "s": 45, "t": 46, "u": 47, "v": 48, "w": 49, "x": 50, "y": 51, "z": 52,
    "à": 53, "â": 54, "ä": 55, "é": 56, "è": 57, "ê": 58, "ë": 59, "î": 60, "ï": 61,
    "ô": 62, "œ": 63, "ù": 64, "û": 65, "ü": 66, "ç": 67,
    "!": 68, "?": 69,
    ",": 70, ".": 71, ";": 72, ":": 73, '"': 74, "'": 75,
    "0": 76, "1": 77, "2": 78, "3": 79, "4": 80, "5": 81, "6": 82, "7": 83, "8": 84, "9": 85,
    " ": 86
}

texto = input("Saisissez le texte à crypter : ")

numeros = []
for caracter in texto:
    if caracter in caracteres:
        numeros.append(caracteres[caracter])

resultados = []
for numero in numeros:
    resultado = numero * 2 + 2
    resultados.append(resultado)

print(" ".join(str(resultado) for resultado in resultados))