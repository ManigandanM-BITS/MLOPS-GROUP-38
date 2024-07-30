"""
This module contains tests for the model training code.
"""

from src.model import load_data

def test_load_data():
    """Test the load_data function."""
    data, target = load_data()
    assert data is not None, "Data should not be None"
    assert target is not None, "Target should not be None"
    assert len(data) == len(target), "Data and Target should be of the same length"

if __name__ == "__main__":
    test_load_data()

