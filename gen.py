import random

def generate_test_cases():
    N = 1000000

    data_sorted = sorted([random.randint(0, 1000000) for _ in range(N)])
    with open("01.txt", "w") as f:
        f.write("\n".join(map(str, data_sorted)))

    rev = sorted([random.randint(0, 1000000) for _ in range(N)])
    data_reversed = rev[::-1]
    with open("02.txt", "w") as f:
        f.write("\n".join(map(str, data_reversed)))

    for i in range(3, 8):
        data = [random.uniform(0, 1000000) for _ in range(N)]
        with open(f"{i:02d}.txt", "w") as f:
            f.write("\n".join(map(str, data)))

    for i in range(8, 11):
        data = [random.randint(0, 1000000) for _ in range(N)]
        with open(f"{i:02d}.txt", "w") as f:
            f.write("\n".join(map(str, data)))
            
generate_test_cases()
