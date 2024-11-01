import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from myPackage import myModule


def test_top_n_items():
    """
    Make sure top_n works correctly
    """
    assert myModule.top_n_items([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert myModule.top_n_items([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myModule.top_n_items([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'
