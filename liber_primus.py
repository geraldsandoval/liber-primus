
rune_to_english = {
    "ᚠ": ["F", 0],
    "ᚢ": ["V(U)", 1],
    "ᚦ": ["TH", 2],
    "ᚩ": ["O", 3],
    "ᚱ": ["R", 4],
    "ᚳ": ["C(K)", 5],
    "ᚷ": ["G", 6],
    "ᚹ": ["W", 7],
    "ᚻ": ["H", 8],
    "ᚾ": ["N", 9],
    "ᛁ": ["I", 10],
    "ᛄ": ["J", 11],
    "ᛇ": ["EO", 12],
    "ᛈ": ["P", 13],
    "ᛉ": ["X", 14],
    "ᛋ": ["S(Z)", 15],
    "ᛏ": ["T", 16],
    "ᛒ": ["B", 17],
    "ᛖ": ["E", 18],
    "ᛗ": ["M", 19],
    "ᛚ": ["L", 20],
    "ᛝ": ["NG(ING)", 21],
    "ᛟ": ["OE", 22],
    "ᛞ": ["D", 23],
    "ᚪ": ["A", 24],
    "ᚫ": ["AE", 25],
    "ᚣ": ["Y", 26],
    "ᛡ": ["IA(IO)", 27],
    "ᛠ": ["EA", 28]
}

dec_to_rune = {
    0: ["ᚠ", "F"],
    1: ["ᚢ", "V(U)"],
    2: ["ᚦ", "TH"],
    3: ["ᚩ", "O"],
    4: ["ᚱ", "R"],
    5: ["ᚳ", "C(K)"],
    6: ["ᚷ", "G"],
    7: ["ᚹ", "W"],
    8: ["ᚻ", "H"],
    9: ["ᚾ", "N"],
    10: ["ᛁ", "I"],
    11: ["ᛄ", "J"],
    12: ["ᛇ", "EO"],
    13: ["ᛈ", "P"],
    14: ["ᛉ", "X"],
    15: ["ᛋ", "S(Z)"],
    16: ["ᛏ", "T"],
    17: ["ᛒ", "B"],
    18: ["ᛖ", "E"],
    19: ["ᛗ", "M"],
    20: ["ᛚ", "L"],
    21: ["ᛝ", "NG(ING)"],
    22: ["ᛟ", "OE"],
    23: ["ᛞ", "D"],
    24: ["ᚪ", "A"],
    25: ["ᚫ", "AE"],
    26: ["ᚣ", "Y"],
    27: ["ᛡ", "IA(IO)"],
    28: ["ᛠ", "EA"]
}

english_to_rune = {
    "F": ["ᚠ", 0],
    "V": ["ᚢ", 1],
    "U": ["ᚢ", 1],
    "TH": ["ᚦ", 2],
    "O": ["ᚩ", 3],
    "R": ["ᚱ", 4],
    "C": ["ᚳ", 5],
    "K": ["ᚳ", 5],
    "G": ["ᚷ", 6],
    "W": ["ᚹ", 7],
    "H": ["ᚻ", 8],
    "N": ["ᚾ", 9],
    "I": ["ᛁ", 10],
    "J": ["ᛄ", 11],
    "EQ": ["ᛇ", 12],
    "P": ["ᛈ", 13],
    "X": ["ᛉ", 14],
    "S": ["ᛋ", 15],
    "Z": ["ᛋ", 15],
    "T": ["ᛏ", 16],
    "B": ["ᛒ", 17],
    "E": ["ᛖ", 18],
    "M": ["ᛗ", 19],
    "L": ["ᛚ", 20],
    "NG(ING)": ["ᛝ", 21],
    "OE": ["ᛟ", 22],
    "D": ["ᛞ", 23],
    "A": ["ᚪ", 24],
    "AE": ["ᚫ", 25],
    "Y": ["ᚣ", 26],
    "IA(IO)": ["ᛡ", 27],
    "EA": ["ᛠ", 28]
}


def open_txt(filename):
    with open(filename, "r") as f:
        txt = f.read()
    return txt


def runes_to_decimals(filename):
    runes = open_txt(filename)
    decimals = []
    for rune in runes:
        #if isinstance(rune, int):
        if rune not in ["-", ".", "/", "&", "%", "§", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n", "\t"]:
            decimals.append(rune_to_english[rune][1])
        else:
            decimals.append(rune)
    return decimals


def decimal_to_english(decimals):
    english = ""
    for item in decimals:
        if isinstance(item, int):
            english += dec_to_rune[item % 28][1]
        else:
            english += item
    return english


def atbash(cipher_text):
    decrypted = []
    for rune in cipher_text:
        if isinstance(rune, int):
                decrypted.append(28 - rune)
        else:
            decrypted.append(rune)
    return decrypted


def eng2rune(english):
    rune = ""
    for letter in english:
        rune += english_to_rune[letter][0]
    return rune


def make_vigenere_key(cipher_text, rune_key, skip):
    num_runes = 0
    num_skipped = 0
    encrypt_key = []
    for index, rune in enumerate(cipher_text):
        if index in skip:
            num_skipped += 1
        if isinstance(rune, int):
            encrypt_key.append(rune_to_english[rune_key[(num_runes - num_skipped) % (len(rune_key))]][1])
            num_runes += 1
        else:
            encrypt_key.append(rune)
    return encrypt_key


def vigenere(cipher_text, key, skip_indices):
    rune_key = eng2rune(key)
    clear_text = []
    encrypt_key = make_vigenere_key(cipher_text, rune_key, skip_indices)
    for index, rune in enumerate(cipher_text):
        if index in skip_indices:
            clear_text.append(rune)
        elif isinstance(rune, int):
            clear_text.append((rune - encrypt_key[index]) % 29)
        else:
            clear_text.append(rune)
    return clear_text


def direct(cipher_text):
    return decimal_to_english(cipher_text)


def shift(cipher, amount):
    shifted_cipher = []
    for rune in cipher:
        if isinstance(rune, int):
            shifted_cipher.append((rune + amount) % 28)
        else:
            shifted_cipher.append(rune)
    return shifted_cipher


def decode_welcome():
    welcome = runes_to_decimals("./Liber Primus Text/welcome.txt")
    print(decimal_to_english(vigenere(welcome, "DIVINITY", [62, 102, 115, 181, 217, 218, 333, 566, 596, 625, 689])))


def decode_a_warning():
    a_warning = runes_to_decimals("./Liber Primus Text/a_warning.txt")
    print(decimal_to_english(atbash(a_warning)))


def decode_koan_1():
    koan_1 = runes_to_decimals("./Liber Primus Text/koan_1.txt")
    print(decimal_to_english(shift(atbash(koan_1), 3)))


def decode_some_wisdom():
    some_wisdom = runes_to_decimals("./Liber Primus Text/some_wisdom.txt")
    print(direct(some_wisdom))


def main():
    decode_some_wisdom()


if __name__ == "__main__":
    main()

