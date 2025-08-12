import numpy as np

def calc_mean(arr):
    return np.mean(arr)

if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5])
    print("Mean:", calc_mean(data))
