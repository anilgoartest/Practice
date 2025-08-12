from main import calc_mean
import numpy as np

def test_mean():
    data = np.array([1, 2, 3, 4, 5])
    assert calc_mean(data) == 3.0
