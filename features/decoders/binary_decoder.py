from chepy import Chepy


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
    # Test with a simple binary encoded string
    test_string = "0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100"  # "Hello World" in binary
    try:
        # Decode as string (default)
        decoded_str = decode_binary_chepy(test_string)
        print(f"Encoded: {test_string}")
        print(f"Decoded as string: {decoded_str}")

        # Decode as bytes
        decoded_bytes = decode_binary_chepy(test_string, as_string=False)
        print(f"Decoded as bytes: {decoded_bytes}")

        # Test with another example
        test_string2 = "0101010001101000011010010111001100100000011010010111001100100000011000010010000001110100011001010111001101110100"  # "This is a test" in binary
        decoded_str2 = decode_binary_chepy(test_string2)
        print(f"Encoded: {test_string2}")
        print(f"Decoded as string: {decoded_str2}")

    except Exception as e:
        print(f"Error: {e}")
