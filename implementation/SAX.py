import string
import numpy as np
import pandas as pd
import time
import math
import multiprocessing

windowSize = 100
alphabetSize = 3

def _reduceHelper(i, values):
    beg = i * windowSize
    end = (i + 1) * windowSize
    seg = values[beg:end]
    N = len(values)
    seg = np.float32(np.sum(seg) * windowSize / N)
    return seg


def reduceDim(values):
    print("length: ", len(values))
    numOfSeg = int(math.ceil(len(values) / windowSize))
    print("Number of Segments:", numOfSeg)
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    reducedTS = pd.Series(pool.starmap(_reduceHelper, [[i, values] for i in range(numOfSeg)]), dtype=np.float32)
    return reducedTS

def _symbolHelper(paa, table):
    for i in range(alphabetSize):
        if paa > table[i] and paa <= table[i + 1]:
            return string.ascii_lowercase[i]

def genSymbol(paa, mean, std):
    breakPoints = {3: [-np.inf, -0.43, 0.43, np.inf],
                   4: [-np.inf, -0.67, 0, 0.67, np.inf],
                   5: [-np.inf, -0.84, -0.25, 0.25, 0.84, np.inf],
                   6: [-np.inf, -0.97, -0.43, 0, 0.43, 0.97, np.inf],
                   7: [-np.inf, -1.07, -0.57, -0.18, 0.18, 0.57, 1.07, np.inf],
                   8: [-np.inf, -1.15, -0.67, -0.32, 0, 0.32, 0.67, 1.15, np.inf],
                   9: [-np.inf, -1.22, -0.76, -0.43, -0.14, 0.14, 0.43, 0.76, 1.22, np.inf],
                   10: [-np.inf, -1.28, -0.84, -0.52, -0.25, 0, 0.25, 0.52, 0.84, 1.28, np.inf],
                   11: [-np.inf, -1.34, -0.91, -0.6, -0.35, -0.11, 0.11, 0.35, 0.6, 0.91, 1.34, np.inf],
                   12: [-np.inf, -1.38, -0.97, -0.67, -0.43, -0.21, 0, 0.21, 0.43, 0.67, 0.97, 1.38, np.inf],
                   13: [-np.inf, -1.43, -1.02, -0.74, -0.5, -0.29, -0.1, 0.1, 0.29, 0.5, 0.74, 1.02, 1.43, np.inf],
                   14: [-np.inf, -1.47, -1.07, -0.79, -0.57, -0.37, -0.18, 0, 0.18, 0.37, 0.57, 0.79, 1.07, 1.47,
                        np.inf],
                   15: [-np.inf, -1.5, -1.11, -0.84, -0.62, -0.43, -0.25, -0.08, 0.08, 0.25, 0.43, 0.62, 0.84, 1.11,
                        1.5, np.inf],
                   16: [-np.inf, -1.53, -1.15, -0.89, -0.67, -0.49, -0.32, -0.16, 0, 0.16, 0.32, 0.49, 0.67, 0.89, 1.15,
                        1.53, np.inf],
                   17: [-np.inf, -1.56, -1.19, -0.93, -0.72, -0.54, -0.38, -0.22, -0.07, 0.07, 0.22, 0.38, 0.54, 0.72,
                        0.93, 1.19, 1.56, np.inf],
                   18: [-np.inf, -1.59, -1.22, -0.97, -0.76, -0.59, -0.43, -0.28, -0.14, 0, 0.14, 0.28, 0.43, 0.59,
                        0.76, 0.97, 1.22, 1.59, np.inf],
                   19: [-np.inf, -1.62, -1.25, -1, -0.8, -0.63, -0.48, -0.34, -0.2, -0.07, 0.07, 0.2, 0.34, 0.48, 0.63,
                        0.8, 1, 1.25, 1.62, np.inf],
                   20: [-np.inf, -1.64, -1.28, -1.04, -0.84, -0.67, -0.52, -0.39, -0.25, -0.13, 0, 0.13, 0.25, 0.39,
                        0.52, 0.67, 0.84, 1.04, 1.28, 1.64, np.inf]}
    breakPoints = breakPoints[alphabetSize]
    symbols = pd.Series()
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores)
    symbols = pd.Series(pool.starmap(_symbolHelper, [[(value-mean)/std, breakPoints] for value in paa]))
    return symbols

if __name__ == "__main__":
    start = time.time()

    dataFile = "middata"
    df = pd.read_csv(dataFile,header=None, dtype=np.float32, engine='c')

    print("Read data:", time.time() - start)

    values = df[0]
    print("Type:", type(values))
    print("length:", len(values))
    mean = values.mean()
    print("mean:", mean)
    std = values.std()
    print("std:", std)

    reducedTS = reduceDim(values)
    symbols = genSymbol(reducedTS, mean, std)
    # print(symbols)
    print("Symbol generated:", time.time() - start)
    symbols.to_csv(dataFile+"Symbols", header=False)

    print("Execution time: ", time.time() - start)