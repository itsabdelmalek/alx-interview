#!/usr/bin/python3
"""
UTF-8 Validation code
"""


def validUTF8(data) -> bool:
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): A list of integers representing a data set where
        each integer represents 1 byte of data

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    remaining_bytes = 0

    for byte in data:
        current_bit = 1 << 7

        if not remaining_bytes:
            while byte & current_bit:
                remaining_bytes += 1
                current_bit >>= 1

            if not remaining_bytes:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            if byte >> 6 != 0b10:
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
