import time
import numpy as np

def main():
    with open("10.txt", "r") as f:
        data = f.read().split()
    numbers = list(map(float, data))
    numbers = np.sort(numbers)
    # for number in numbers:
    #     if number.is_integer():
    #         print(int(number), end = " ")
    #     else:
    #         print(number, end = " ")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(end_time - start_time)