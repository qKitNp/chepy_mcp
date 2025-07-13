from chepy import Chepy


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
