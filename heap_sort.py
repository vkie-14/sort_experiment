import time
def heapify(numbers, length, i):
    largest = i 
    left = 2 * i + 1
    right = 2 * i + 2
    if left < length and numbers[left] > numbers[largest]:
        largest = left
    # Kiểm tra con trái.
    if right < length and numbers[right] > numbers[largest]:
        largest = right
    # Kiểm tra con phải.
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i] 
        heapify(numbers, length, largest)

def heap_sort(numbers):
    length = len(numbers)
    for i in range(length // 2 - 1, -1, -1):
        heapify(numbers, length, i)
    # Max heap.

    for i in range(length - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i] 
        # Đưa gốc về cuối mảng.
        heapify(numbers, i, 0)

def main():
    with open("10.txt", "r") as f:
        data = f.read().split()
    numbers = list(map(float, data))
    heap_sort(numbers)
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