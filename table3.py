#!/usr/bin/env python3
"""
Multiplication table of 3
"""

def print_table_of_3(limit=10):
    """
    Print the multiplication table of 3 up to the given limit.
    
    Args:
        limit (int): The maximum multiplier (default: 10)
    """
    print("Multiplication Table of 3")
    print("=" * 30)
    
    for i in range(1, limit + 1):
        result = 3 * i
        print(f"3 × {i} = {result}")
    
    print("=" * 30)


if __name__ == "__main__":
    # Print table of 3 up to 10
    print_table_of_3()
    
    # Optional: Print table with a custom limit
    print("\nTable of 3 (up to 15):")
    print_table_of_3(15)
