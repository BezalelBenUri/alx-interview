#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    buffer_size = 1

    while buffer_size < n:
        if n % buffer_size == 0:
            clipboard = buffer_size
            operations += 1
        buffer_size += clipboard
        operations += 1

    return operations
