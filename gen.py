import random

def generate_test_cases():
    N = 1000000
    
    # 1. Dãy số thực tăng dần
    print("Đang sinh dãy tăng dần...")
    data_sorted = sorted([random.randint(0, 1000000) for _ in range(N)])
    with open("01.txt", "w") as f:
        f.write("\n".join(map(str, data_sorted)))

    # 2. Dãy số thực giảm dần
    print("Đang sinh dãy giảm dần...")
    rev = sorted([random.randint(0, 1000000) for _ in range(N)])
    data_reversed = rev[::-1]
    with open("02.txt", "w") as f:
        f.write("\n".join(map(str, data_reversed)))

    # 3. 3 dãy số thực ngẫu nhiên
    for i in range(3, 8):
        print(f"Đang sinh dãy thực ngẫu nhiên {i}...")
        data = [random.uniform(0, 1000000) for _ in range(N)]
        with open(f"{i:02d}.txt", "w") as f:
            f.write("\n".join(map(str, data)))

    # 4. 5 dãy số nguyên ngẫu nhiên
    for i in range(8, 11):
        print(f"Đang sinh dãy nguyên ngẫu nhiên {i}...")
        data = [random.randint(0, 1000000) for _ in range(N)]
        with open(f"{i:02d}.txt", "w") as f:
            f.write("\n".join(map(str, data)))

    print("--- Xong! ---")

generate_test_cases()