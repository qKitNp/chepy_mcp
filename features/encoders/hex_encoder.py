from chepy import Chepy


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


def demo_encode_decode():
    """
    Demonstrate how to use the encoder with the decoder from hex_decoder.py
    """
    try:
        # Try different import approaches
        try:
            from features.decoders.hex_decoder import decode_hex_chepy
        except ImportError:
            from decoders.hex_decoder import decode_hex_chepy

        print("🔄 Demonstrating hex encode/decode round-trip:")
        print("=" * 50)

        test_string = "Hello, this is a test message! 🚀"
        print(f"Original: {test_string}")

        # Encode
        encoded = encode_hex_chepy(test_string)
        print(f"Encoded:  {encoded}")

        # Decode back
        decoded = decode_hex_chepy(encoded)
        print(f"Decoded:  {decoded}")

        # Verify they match
        matches = test_string == decoded
        print(f"Match:    {matches} {'✅' if matches else '❌'}")

    except ImportError:
        print(
            "⚠️  hex_decoder.py not found. Please ensure it exists in the features directory."
        )
    except Exception as e:
        print(f"❌ Error: {e}")


# Example usage
if __name__ == "__main__":
    # Test with a simple string
    test_string = "Hello World"
    try:
        # Encode as string (default)
        encoded_str = encode_hex_chepy(test_string)
        print(f"Original: {test_string}")
        print(f"Encoded as string: {encoded_str}")

        # Encode as bytes
        encoded_bytes = encode_hex_chepy(test_string, as_string=False)
        print(f"Encoded as bytes: {encoded_bytes}")

        # Test with another example
        test_string2 = "This is a test"
        encoded_str2 = encode_hex_chepy(test_string2)
        print(f"Original: {test_string2}")
        print(f"Encoded as string: {encoded_str2}")

        # Test with special characters
        test_string3 = "Hello, 世界! 🌍"
        encoded_str3 = encode_hex_chepy(test_string3)
        print(f"Original: {test_string3}")
        print(f"Encoded as string: {encoded_str3}")

        print("\n" + "=" * 50)
        demo_encode_decode()

    except Exception as e:
        print(f"Error: {e}")
