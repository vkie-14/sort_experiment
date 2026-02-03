import time
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers # Kết thúc đệ quy.
    pivot = numbers[len(numbers)//2]
    left_numbers, right_numbers, middle_numbers = [], [], []
    for number in numbers:
        if number < pivot:
            left_numbers.append(number)
        elif number > pivot:
            right_numbers.append(number)
        else:
            middle_numbers.append(number)
    # Chia dãy số làm 3 phần: nhỏ hơn, lớn hơn và bằng pivot.

    return quick_sort(left_numbers) + middle_numbers + quick_sort(right_numbers)
    # Ghép dãy lại sau khi sắp xếp.

def main():
    with open("10.txt", "r") as f:
        data = f.read().split()
    numbers = list(map(float, data))
    numbers = quick_sort(numbers)
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