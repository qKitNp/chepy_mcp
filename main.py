from fastmcp import FastMCP
from features.encoders import (
    encode_base64_chepy,
    encode_base32_chepy,
    encode_base58_chepy,
    encode_base85_chepy,
    encode_ascii85_chepy,
    encode_url_chepy,
    encode_hex_chepy,
    encode_binary_chepy,
)
from features.decoders import (
    decode_base64_chepy,
    decode_base32_chepy,
    decode_base58_chepy,
    decode_base85_chepy,
    decode_ascii85_chepy,
    decode_url_chepy,
    decode_hex_chepy,
    decode_binary_chepy,
)
from features.ciphers import (
    rot13_encode,
    caesar_encrypt,
    atbash_encode,
    rail_fence_encrypt,
    vigenere_encrypt,
    morse_encode,
)
from features.deciphers import (
    rot13_decode,
    caesar_decrypt,
    atbash_decode,
    rail_fence_decrypt,
    vigenere_decrypt,
    morse_decode,
)
from enum import Enum

mcp = FastMCP()


class EncoderType(str, Enum):
    """Available encoding types for the encoder and decoder tools."""

    BASE64 = "base64"
    BASE32 = "base32"
    BASE58 = "base58"
    BASE85 = "base85"
    ASCII85 = "ascii85"
    URL = "url"
    HEX = "hex"
    BINARY = "binary"


@mcp.tool()
def encoder(
    input_string: str, encoder_type: EncoderType, as_string: bool = True
) -> str:
    """
    Encode a string using various encoding formats.

    This tool can encode strings using 8 different encoding formats:
    - base64: Standard base64 encoding (A-Z, a-z, 0-9, +, /)
    - base32: Base32 encoding (A-Z, 2-7)
    - base58: Bitcoin-style base58 encoding (alphanumeric without 0, O, I, l)
    - base85: Adobe-style base85 encoding
    - ascii85: ASCII85 encoding (similar to base85)
    - url: URL percent encoding (e.g., spaces become %20)
    - hex: Hexadecimal encoding (0-9, a-f)
    - binary: Binary encoding (0s and 1s)

    Args:
        input_string (str): The string to encode. Can contain any characters including Unicode, emojis, and special symbols.
        encoder_type (EncoderType): The type of encoding to use. Must be one of: base64, base32, base58, base85, ascii85, url, hex, binary
        as_string (bool): If True, return the result as a string. If False, return as bytes. Default is True.

    Returns:
        str: The encoded string in the specified format

    Examples:
        - encoder("Hello World", "base64") → "SGVsbG8gV29ybGQ="
        - encoder("Hello World", "hex") → "48656c6c6f20576f726c64"
        - encoder("Hello World", "binary") → "0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100"
        - encoder("Hello World", "url") → "Hello%20World"

    Raises:
        Exception: If encoding fails or an unsupported encoder type is provided
    """
    try:
        if encoder_type == EncoderType.BASE64:
            return encode_base64_chepy(input_string, as_string)
        elif encoder_type == EncoderType.BASE32:
            return encode_base32_chepy(input_string, as_string)
        elif encoder_type == EncoderType.BASE58:
            return encode_base58_chepy(input_string, as_string)
        elif encoder_type == EncoderType.BASE85:
            return encode_base85_chepy(input_string, as_string)
        elif encoder_type == EncoderType.ASCII85:
            return encode_ascii85_chepy(input_string, as_string)
        elif encoder_type == EncoderType.URL:
            return encode_url_chepy(input_string, as_string)
        elif encoder_type == EncoderType.HEX:
            return encode_hex_chepy(input_string, as_string)
        elif encoder_type == EncoderType.BINARY:
            return encode_binary_chepy(input_string, as_string)
        else:
            raise Exception(f"Unsupported encoder type: {encoder_type}")
    except Exception as e:
        raise Exception(f"Failed to encode string using {encoder_type}: {e}")


@mcp.tool()
def decoder(
    encoded_string: str, decoder_type: EncoderType, as_string: bool = True
) -> str:
    """
    Decode a string that was encoded using various encoding formats.

    This tool can decode strings that were encoded using 8 different formats:
    - base64: Decodes standard base64 encoded strings (A-Z, a-z, 0-9, +, /)
    - base32: Decodes base32 encoded strings (A-Z, 2-7)
    - base58: Decodes Bitcoin-style base58 encoded strings (alphanumeric without 0, O, I, l)
    - base85: Decodes Adobe-style base85 encoded strings
    - ascii85: Decodes ASCII85 encoded strings (similar to base85)
    - url: Decodes URL percent encoded strings (e.g., %20 becomes space)
    - hex: Decodes hexadecimal encoded strings (0-9, a-f)
    - binary: Decodes binary encoded strings (0s and 1s)

    Args:
        encoded_string (str): The encoded string to decode. Must be a valid encoded string in the specified format.
        decoder_type (EncoderType): The type of decoding to use. Must match the encoding format used originally. Must be one of: base64, base32, base58, base85, ascii85, url, hex, binary
        as_string (bool): If True, return the result as a string. If False, return as bytes. Default is True.

    Returns:
        str: The decoded original string

    Examples:
        - decoder("SGVsbG8gV29ybGQ=", "base64") → "Hello World"
        - decoder("48656c6c6f20576f726c64", "hex") → "Hello World"
        - decoder("0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100", "binary") → "Hello World"
        - decoder("Hello%20World", "url") → "Hello World"

    Raises:
        Exception: If decoding fails, the input is not valid for the specified format, or an unsupported decoder type is provided
    """
    try:
        if decoder_type == EncoderType.BASE64:
            return decode_base64_chepy(encoded_string, as_string)
        elif decoder_type == EncoderType.BASE32:
            return decode_base32_chepy(encoded_string, as_string)
        elif decoder_type == EncoderType.BASE58:
            return decode_base58_chepy(encoded_string, as_string)
        elif decoder_type == EncoderType.BASE85:
            return decode_base85_chepy(encoded_string, as_string)
        elif decoder_type == EncoderType.ASCII85:
            return decode_ascii85_chepy(encoded_string, as_string)
        elif decoder_type == EncoderType.URL:
            return decode_url_chepy(encoded_string, as_string)
        elif decoder_type == EncoderType.HEX:
            return decode_hex_chepy(encoded_string, as_string)
        elif decoder_type == EncoderType.BINARY:
            return decode_binary_chepy(encoded_string, as_string)
        else:
            raise Exception(f"Unsupported decoder type: {decoder_type}")
    except Exception as e:
        raise Exception(f"Failed to decode string using {decoder_type}: {e}")


class CipherType(str, Enum):
    ROT13 = "rot13"
    CAESAR = "caesar"
    ATBASH = "atbash"
    RAIL_FENCE = "rail_fence"
    VIGENERE = "vigenere"
    MORSE = "morse"


@mcp.tool()
def cipher(
    input_string: str,
    cipher_type: CipherType,
    key: str = "",
    shift: int = 3,
    num_rails: int = 2,
) -> str:
    """
    Encode a string using classical ciphers (rot13, caesar, atbash, rail fence, vigenere, morse).
    Args:
        input_string (str): The string to encode.
        cipher_type (CipherType): The cipher to use.
        key (str): The key for vigenere cipher (required for vigenere).
        shift (int): The shift for caesar cipher (default 3).
        num_rails (int): The number of rails for rail fence cipher (default 2).
    Returns:
        str: The encoded string.
    """
    if cipher_type == CipherType.ROT13:
        return rot13_encode(input_string)
    elif cipher_type == CipherType.CAESAR:
        return caesar_encrypt(input_string, shift)
    elif cipher_type == CipherType.ATBASH:
        return atbash_encode(input_string)
    elif cipher_type == CipherType.RAIL_FENCE:
        return rail_fence_encrypt(input_string, num_rails)
    elif cipher_type == CipherType.VIGENERE:
        if not key:
            raise ValueError("Key is required for vigenere cipher.")
        return vigenere_encrypt(input_string, key)
    elif cipher_type == CipherType.MORSE:
        return morse_encode(input_string)
    else:
        raise ValueError(f"Unsupported cipher type: {cipher_type}")


@mcp.tool()
def decipher(
    input_string: str,
    cipher_type: CipherType,
    key: str = "",
    shift: int = 3,
    num_rails: int = 2,
) -> str:
    """
    Decode a string using classical ciphers (rot13, caesar, atbash, rail fence, vigenere, morse).
    Args:
        input_string (str): The string to decode.
        cipher_type (CipherType): The cipher to use.
        key (str): The key for vigenere cipher (required for vigenere).
        shift (int): The shift for caesar cipher (default 3).
        num_rails (int): The number of rails for rail fence cipher (default 2).
    Returns:
        str: The decoded string.
    """
    if cipher_type == CipherType.ROT13:
        return rot13_decode(input_string)
    elif cipher_type == CipherType.CAESAR:
        return caesar_decrypt(input_string, shift)
    elif cipher_type == CipherType.ATBASH:
        return atbash_decode(input_string)
    elif cipher_type == CipherType.RAIL_FENCE:
        return rail_fence_decrypt(input_string, num_rails)
    elif cipher_type == CipherType.VIGENERE:
        if not key:
            raise ValueError("Key is required for vigenere cipher.")
        return vigenere_decrypt(input_string, key)
    elif cipher_type == CipherType.MORSE:
        return morse_decode(input_string)
    else:
        raise ValueError(f"Unsupported cipher type: {cipher_type}")


if __name__ == "__main__":
    mcp.run()
