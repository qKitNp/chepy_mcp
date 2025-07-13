from chepy import Chepy


def encode_base64_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to base64 using chepy.

    Args:
        input_string (str): The string to encode to base64
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The base64 encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to base64
        result = Chepy(input_string).to_base64().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to base64: {e}")


def encode_base32_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to base32 using chepy.

    Args:
        input_string (str): The string to encode to base32
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The base32 encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to base32
        result = Chepy(input_string).to_base32().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to base32: {e}")


def encode_base58_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to base58 using chepy.

    Args:
        input_string (str): The string to encode to base58
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The base58 encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to base58
        result = Chepy(input_string).to_base58().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to base58: {e}")


def encode_base85_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to base85 using chepy.

    Args:
        input_string (str): The string to encode to base85
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The base85 encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to base85
        result = Chepy(input_string).to_base85().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to base85: {e}")


def encode_ascii85_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to ASCII85 using chepy.

    Args:
        input_string (str): The string to encode to ASCII85
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The ASCII85 encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to ASCII85
        result = Chepy(input_string).to_ascii85().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to ASCII85: {e}")


def encode_url_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to URL encoding using chepy.

    Args:
        input_string (str): The string to encode to URL encoding
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The URL encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to URL
        result = Chepy(input_string).url_encode().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to URL: {e}")


def encode_hex_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to hex using chepy.

    Args:
        input_string (str): The string to encode to hex
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The hex encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to hex
        result = Chepy(input_string).to_hex().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to hex: {e}")


def encode_binary_chepy(input_string: str, as_string: bool = True) -> str:
    """
    Encode a string to binary using chepy.

    Args:
        input_string (str): The string to encode to binary
        as_string (bool): If True, return as string; if False, return as bytes

    Returns:
        str or bytes: The binary encoded result

    Raises:
        Exception: If encoding fails
    """
    try:
        # Create a Chepy instance with the input string and encode to binary
        result = Chepy(input_string).to_binary().o

        # Convert to string if requested and result is bytes
        if as_string and isinstance(result, bytes):
            result = result.decode("utf-8")

        return result
    except Exception as e:
        raise Exception(f"Failed to encode string to binary: {e}")


# Example usage
if __name__ == "__main__":
    # Test with a simple string
    test_string = "Hello World"
    try:
        # Test all encoders
        print("Testing all encoders:")
        print("=" * 50)

        print(f"Original: {test_string}")
        print(f"Base64:   {encode_base64_chepy(test_string)}")
        print(f"Base32:   {encode_base32_chepy(test_string)}")
        print(f"Base58:   {encode_base58_chepy(test_string)}")
        print(f"Base85:   {encode_base85_chepy(test_string)}")
        print(f"ASCII85:  {encode_ascii85_chepy(test_string)}")
        print(f"URL:      {encode_url_chepy(test_string)}")
        print(f"Hex:      {encode_hex_chepy(test_string)}")
        print(f"Binary:   {encode_binary_chepy(test_string)}")

    except Exception as e:
        print(f"Error: {e}")
