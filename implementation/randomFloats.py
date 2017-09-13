import numpy as np
import time
if __name__ == "__main__":
    start = time.time()
    size = 10000000
    with open("middata", 'w') as file:
        for _ in range(size):
            file.write(str(np.random.random_sample() * 10 - 5) + "\n")
    print(time.time() - start)