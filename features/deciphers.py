import string

# ROT13


def rot13_decode(input_string: str) -> str:
    """Decode a string using ROT13 cipher (same as encode)."""
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


def caesar_decrypt(input_string: str, shift: int = 3) -> str:
    """Decrypt a string using Caesar cipher with a given shift (default 3)."""

    def shift_char(c):
        if c.isupper():
            return chr((ord(c) - 65 - shift) % 26 + 65)
        elif c.islower():
            return chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            return c

    return "".join(shift_char(c) for c in input_string)


# Atbash


def atbash_decode(input_string: str) -> str:
    """Decode a string using Atbash cipher (same as encode)."""

    def atbash_char(c):
        if c.isupper():
            return chr(90 - (ord(c) - 65))
        elif c.islower():
            return chr(122 - (ord(c) - 97))
        else:
            return c

    return "".join(atbash_char(c) for c in input_string)


# Rail Fence


def rail_fence_decrypt(ciphertext: str, num_rails: int = 2) -> str:
    """Decrypt a string using Rail Fence cipher with a given number of rails (default 2)."""
    if num_rails <= 1:
        return ciphertext
    # Calculate the pattern
    pattern = [0] * len(ciphertext)
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        pattern[i] = rail
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    # Count how many chars per rail
    rail_counts = [pattern.count(r) for r in range(num_rails)]
    # Split the ciphertext into rails
    rails = []
    idx = 0
    for count in rail_counts:
        rails.append(ciphertext[idx : idx + count])
        idx += count
    # Reconstruct the plaintext
    result = []
    rail_indices = [0] * num_rails
    for r in pattern:
        result.append(rails[r][rail_indices[r]])
        rail_indices[r] += 1
    return "".join(result)


# Vigenere


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt a string using Vigenère cipher with a given key."""
    key = key.lower()
    result = []
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                result.append(chr((ord(char) - 65 - shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 - shift) % 26 + 97))
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
MORSE_CODE_DICT_REVERSE = {v: k for k, v in MORSE_CODE_DICT.items()}


def morse_decode(morse_code: str) -> str:
    """Decode a Morse code string to text."""
    return "".join(
        MORSE_CODE_DICT_REVERSE.get(code, "") for code in morse_code.split(" ")
    )
