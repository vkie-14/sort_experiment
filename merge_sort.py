import time
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Ghép hai mảng leff và right đã được sắp xếp
    result.extend(left[i:])
    result.extend(right[j:])
    # Ghép nốt phần còn dư
    return result

def main():
    with open("08.txt", "r") as f:
        data = f.read().split()

    numbers = list(map(float, data))
    numbers = merge_sort(numbers)
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
