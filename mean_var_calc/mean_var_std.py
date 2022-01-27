import numpy as np


def calculate(list1):
    if len(list1) != 9:
        raise ValueError("List must contain nine numbers.")

    mat = np.reshape(np.array(list1), (3, 3))

    calculations = {
        'mean': [list(np.mean(mat, axis=0)), list(np.mean(mat, axis=1)), np.mean(mat)],
        'variance': [list(np.var(mat, axis=0)), list(np.var(mat, axis=1)), np.var(mat)],
        'standard deviation': [list(np.std(mat, axis=0)), list(np.std(mat, axis=1)), np.std(mat)],
        'max': [list(np.max(mat, axis=0)), list(np.max(mat, axis=1)), np.max(mat)],
        'min': [list(np.min(mat, axis=0)), list(np.min(mat, axis=1)), np.min(mat)],
        'sum': [list(np.sum(mat, axis=0)), list(np.sum(mat, axis=1)), np.sum(mat)]
    }

    return calculations
