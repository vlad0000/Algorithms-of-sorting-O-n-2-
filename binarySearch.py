my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
def binary_search(my_list, item):

    low = 0
    high = len(my_list) - 1
    mid = (high + low) // 2
    guess = my_list[mid]

    while low <= high:
        mid = (high + low) // 2
        guess = my_list[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search(my_list, 0))
