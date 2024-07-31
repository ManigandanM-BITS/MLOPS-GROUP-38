"""
Main module for demonstrating simple addition operation.
"""

def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    result = a + b
    return result

if __name__ == "__main__":
    print(add(2, 3))
