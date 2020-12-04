import numpy as np


def manual_list(row, col):
    tempArr = []
    for i in range(row):
        print('Baris ke-', (i + 1))
        for j in range(col):
            tempArr.append(float(input('    Elemen: ')))
        print('')
    return np.array(tempArr)


def populate_list(row, col, spread):
    np.set_printoptions(precision=2)
    return np.array(np.random.uniform(1, spread, (row, col)), dtype=float)


def template_list():
    tempArr = [
        [26, 35],
        [13, 12],
        [11, 5],
        [10, 15],
        [50, 45],
        [200, 200],
        [18, 20],
        [21, 14],
        [16, 20],
        [21, 75]
    ]
    return np.array(tempArr)


def proximity_matrix(A, B):
    kuadratA = (A ** 2).sum(axis=1)
    kuadratB = (B ** 2).sum(axis=1).reshape((A.shape[0], 1))
    duaAB = 2 * A.dot(B.T)
    return np.sqrt(abs(kuadratA - duaAB + kuadratB))


def idx_matrix(size):
    tempArr = []
    for i in range(size):
        tempArr.append(np.arange(size))
    return np.array(tempArr)


def nearest_matrix(prxM, idxM):
    for i in range(prxM.shape[0]):
        for j in range(prxM.shape[1]):
            for k in range(prxM.shape[1] - j - 1):
                if (prxM[i, k] > prxM[i, k + 1]):
                    prxM[i, k], prxM[i, k + 1] = prxM[i, k + 1], prxM[i, k]
                    idxM[i, k], idxM[i, k + 1] = idxM[i, k + 1], idxM[i, k]


def average_density(K, valueTrim):
    np.set_printoptions(precision=5)
    avgDens = K / valueTrim.sum(axis=1)
    return avgDens.reshape((avgDens.shape[0], 1))


def average_rel_dens(indexTrim, avgDens, K):
    tempArr = []
    for i in range(avgDens.shape[0]):
        totDens = 0
        for j in range(indexTrim.shape[1]):
            totDens += avgDens[indexTrim[i, j]]
        tempArr.append(float(totDens / K / avgDens[i]))
    return np.array(tempArr).reshape((avgDens.shape[0], 1))
