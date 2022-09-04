new_alpha = {"a": "@", "b": "8", "c": "(", "d": "|)", "e": "3", "f": "#", "g": "6", "h": "[-]", "i": "|", "j": "_|", "k": "|<", "l": "1", "m": "[]\/[]",
"n": "[]\[]", "o": "0", "p": "|D", "q": "(,)", "r": "|Z", "s": "$", "t": "']['", "u": "|_|", "v": "\/", "w": "\/\/", "x": "}{", "y": "`/", "z": "2"}
sentence = input("").lower()
new_sentence = ""
for e in sentence:
    if e.isalpha():
        new_sentence += new_alpha[e]
    else:
        new_sentence += e

print(new_sentence)