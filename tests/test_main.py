"""
Test cases for main functions.
"""

from model import add, train_model
import os

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_model_training():
    train_model()
    assert os.path.exists('model.pkl')
