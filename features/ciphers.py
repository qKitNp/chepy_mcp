import string

# ROT13


def rot13_encode(input_string: str) -> str:
    """Encode a string using ROT13 cipher."""
    return input_string.translate(
        str.maketrans(
            string.ascii_lowercase + string.ascii_uppercase,
            string.ascii_lowercase[13:]
            + string.ascii_lowercase[:13]
            + string.ascii_uppercase[13:]
            + string.ascii_uppercase[:13],
        )
    )


# Caesar


def caesar_encrypt(input_string: str, shift: int = 3) -> str:
    """Encrypt a string using Caesar cipher with a given shift (default 3)."""

    def shift_char(c):
        if c.isupper():
            return chr((ord(c) - 65 + shift) % 26 + 65)
        elif c.islower():
            return chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            return c

    return "".join(shift_char(c) for c in input_string)


# Atbash


def atbash_encode(input_string: str) -> str:
    """Encode a string using Atbash cipher."""

    def atbash_char(c):
        if c.isupper():
            return chr(90 - (ord(c) - 65))
        elif c.islower():
            return chr(122 - (ord(c) - 97))
        else:
            return c

    return "".join(atbash_char(c) for c in input_string)


# Rail Fence


def rail_fence_encrypt(input_string: str, num_rails: int = 2) -> str:
    """Encrypt a string using Rail Fence cipher with a given number of rails (default 2)."""
    if num_rails <= 1:
        return input_string
    rails = ["" for _ in range(num_rails)]
    rail = 0
    direction = 1
    for char in input_string:
        rails[rail] += char
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    return "".join(rails)


# Vigenere


def vigenere_encrypt(input_string: str, key: str) -> str:
    """Encrypt a string using Vigenère cipher with a given key."""
    key = key.lower()
    result = []
    key_index = 0
    for char in input_string:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


# Morse
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "&": ".-...",
    "@": ".--.-.",
    ":": "---...",
    ",": "--..--",
    ".": ".-.-.-",
    "'": ".----.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "!": "-.-.--",
    " ": "/",
}


def morse_encode(input_string: str) -> str:
    """Encode a string to Morse code."""
    return " ".join(MORSE_CODE_DICT.get(c.upper(), "") for c in input_string)
