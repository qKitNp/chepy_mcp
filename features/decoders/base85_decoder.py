from chepy import Chepy


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


# Example usage
if __name__ == "__main__":
    # Test with a simple base85 encoded string
    test_string = "87cURD]i,E!7,Cl*ARoF`"  # "Hello World" in base85
    try:
        # Decode as string (default)
        decoded_str = decode_base85_chepy(test_string)
        print(f"Encoded: {test_string}")
        print(f"Decoded as string: {decoded_str}")

        # Decode as bytes
        decoded_bytes = decode_base85_chepy(test_string, as_string=False)
        print(f"Decoded as bytes: {decoded_bytes}")

        # Test with another example
        test_string2 = "87cURD]i,E!7,Cl*ARoF`"  # "This is a test" in base85
        decoded_str2 = decode_base85_chepy(test_string2)
        print(f"Encoded: {test_string2}")
        print(f"Decoded as string: {decoded_str2}")

    except Exception as e:
        print(f"Error: {e}")
