# This file makes the features directory a Python package

# Import all encoders from the consolidated encoders file
from .encoders import (
    encode_base64_chepy,
    encode_base32_chepy,
    encode_base58_chepy,
    encode_base85_chepy,
    encode_ascii85_chepy,
    encode_url_chepy,
    encode_hex_chepy,
    encode_binary_chepy,
)

# Import all decoders from the consolidated decoders file
from .decoders import (
    decode_base64_chepy,
    decode_base32_chepy,
    decode_base58_chepy,
    decode_base85_chepy,
    decode_ascii85_chepy,
    decode_url_chepy,
    decode_hex_chepy,
    decode_binary_chepy,
)

# Import all ciphers from ciphers.py
from .ciphers import (
    rot13_encode,
    caesar_encrypt,
    atbash_encode,
    rail_fence_encrypt,
    vigenere_encrypt,
    morse_encode,
)

# Import all deciphers from deciphers.py
from .deciphers import (
    rot13_decode,
    caesar_decrypt,
    atbash_decode,
    rail_fence_decrypt,
    vigenere_decrypt,
    morse_decode,
)

__all__ = [
    # Encoders
    "encode_base64_chepy",
    "encode_base32_chepy",
    "encode_base58_chepy",
    "encode_base85_chepy",
    "encode_ascii85_chepy",
    "encode_url_chepy",
    "encode_hex_chepy",
    "encode_binary_chepy",
    # Ciphers
    "rot13_encode",
    "caesar_encrypt",
    "atbash_encode",
    "rail_fence_encrypt",
    "vigenere_encrypt",
    "morse_encode",
    # Decoders
    "decode_base64_chepy",
    "decode_base32_chepy",
    "decode_base58_chepy",
    "decode_base85_chepy",
    "decode_ascii85_chepy",
    "decode_url_chepy",
    "decode_hex_chepy",
    "decode_binary_chepy",
    # Deciphers
    "rot13_decode",
    "caesar_decrypt",
    "atbash_decode",
    "rail_fence_decrypt",
    "vigenere_decrypt",
    "morse_decode",
]
