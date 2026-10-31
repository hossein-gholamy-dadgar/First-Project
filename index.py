n = input()
matn = int(input())

english_to_persian = {
    "q": "ض",
    "w": "ص",
    "e": "ث",
    "r": "ق",
    "t": "ف",
    "y": "غ",
    "u": "ع",
    "i": "ه",
    "o": "خ",
    "p": "ح",

    "a": "ش",
    "s": "س",
    "d": "ی",
    "f": "ب",
    "g": "ل",
    "h": "ا",
    "j": "ت",
    "k": "ن",
    "l": "م",

    "z": "ظ",
    "x": "ط",
    "c": "ز",
    "v": "ر",
    "b": "ذ",
    "n": "د",
    "m": "ئ",

    "[": "ج",
    "]": "چ",
    ";": "ک",
    "'": "گ",
    ",": "و",
    "\\": "پ",
    "C": "ژ"
}

persian_to_english = {}

for key in english_to_persian:
    value = english_to_persian[key]
    persian_to_english[value] = key

result = ""

if matn == 1:
    d = english_to_persian
else:
    d = persian_to_english

for a in n:
    result += d.get(a,a)

print(result)