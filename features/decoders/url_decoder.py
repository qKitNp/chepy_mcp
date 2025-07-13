from chepy import Chepy


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


# Example usage
if __name__ == "__main__":
    # Test with a simple URL encoded string
    test_string = "Hello%20World"  # "Hello World" in URL encoding
    try:
        # Decode as string (default)
        decoded_str = decode_url_chepy(test_string)
        print(f"Encoded: {test_string}")
        print(f"Decoded as string: {decoded_str}")

        # Decode as bytes
        decoded_bytes = decode_url_chepy(test_string, as_string=False)
        print(f"Decoded as bytes: {decoded_bytes}")

        # Test with another example
        test_string2 = "This%20is%20a%20test"  # "This is a test" in URL encoding
        decoded_str2 = decode_url_chepy(test_string2)
        print(f"Encoded: {test_string2}")
        print(f"Decoded as string: {decoded_str2}")

    except Exception as e:
        print(f"Error: {e}")
