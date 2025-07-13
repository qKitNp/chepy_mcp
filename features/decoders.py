from chepy import Chepy
import string


def decode_base64_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode a base64 encoded string using chepy.

    Args:
        encoded_string (str): The base64 encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid base64 or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).from_base64().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode base64 string: {e}")


def decode_base32_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode a base32 encoded string using chepy.

    Args:
        encoded_string (str): The base32 encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid base32 or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).from_base32().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode base32 string: {e}")


def decode_base58_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode a base58 encoded string using chepy.

    Args:
        encoded_string (str): The base58 encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid base58 or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).from_base58().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode base58 string: {e}")


def decode_base85_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode a base85 encoded string using chepy.

    Args:
        encoded_string (str): The base85 encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid base85 or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).from_base85().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode base85 string: {e}")


def decode_ascii85_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode an ASCII85 encoded string using chepy.

    Args:
        encoded_string (str): The ASCII85 encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid ASCII85 or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).from_ascii85().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode ASCII85 string: {e}")


def decode_url_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode a URL encoded string using chepy.

    Args:
        encoded_string (str): The URL encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid URL encoding or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).url_decode().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode URL string: {e}")


def decode_hex_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode a hex encoded string using chepy.

    Args:
        encoded_string (str): The hex encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid hex or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).from_hex().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode hex string: {e}")


def decode_binary_chepy(encoded_string: str, as_string: bool = True) -> str:
    """
    Decode a binary encoded string using chepy.

    Args:
        encoded_string (str): The binary encoded string to decode
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The decoded result

    Raises:
        Exception: If the input is not valid binary or decoding fails
    """
    try:
        # Create a Chepy instance with the encoded string
        result = Chepy(encoded_string).from_binary().o

        # Convert to string if requested
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to decode binary string: {e}")


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


# Example usage
if __name__ == "__main__":
    # Test with encoded strings
    try:
        # Test all decoders
        print("Testing all decoders:")
        print("=" * 50)

        # Base64 test
        base64_encoded = "SGVsbG8gV29ybGQ="  # "Hello World"
        print(f"Base64 encoded: {base64_encoded}")
        print(f"Base64 decoded: {decode_base64_chepy(base64_encoded)}")

        # Base32 test
        base32_encoded = "JBSWY3DPEBLW64TMMQ======"  # "Hello World"
        print(f"Base32 encoded: {base32_encoded}")
        print(f"Base32 decoded: {decode_base32_chepy(base32_encoded)}")

        # Hex test
        hex_encoded = "48656c6c6f20576f726c64"  # "Hello World"
        print(f"Hex encoded: {hex_encoded}")
        print(f"Hex decoded: {decode_hex_chepy(hex_encoded)}")

        # URL test
        url_encoded = "Hello%20World"  # "Hello World"
        print(f"URL encoded: {url_encoded}")
        print(f"URL decoded: {decode_url_chepy(url_encoded)}")

    except Exception as e:
        print(f"Error: {e}")
