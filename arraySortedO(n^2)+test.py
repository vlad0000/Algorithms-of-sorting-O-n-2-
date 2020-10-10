def choise_sort(my_list):
    '''
    Выполняет сортировку методом выбора.
    Суть алгоритма заключается в том, чтобы с каждым проходом
    определять для каждой позиции минимальное число,
    И в итоге последний элемент становится автоматически отсортированным
    :param my_list: list, неотсортированный список
    :return: my_list - отсортированный список
    '''
    count_item = len(my_list)

    for pos in range (0, count_item - 1):
        for k in range(pos+1, count_item):
            if my_list[k] < my_list[pos]:
                my_list[k], my_list[pos] = my_list[pos], my_list[k]
    return my_list

def insert_sort(my_list):
    '''
    Сортировка методом вставок.
    Суть сортировки заключается в том, чтобы с каждым проходом i сравнивалось с i-1 и
    В случае если i меньше i-1, то они меняются местами и так пока весь массив не отсортируется
    :param my_list: list - не отсортированный список
    :return: my_list - отсортированный список
    '''

    count_item = len(my_list)
    for top in range(1, count_item):
        k = top
        while k > 0 and my_list[k-1] > my_list[k]:
            my_list[k], my_list[k-1] = my_list[k-1], my_list[k]
            k -= 1

    return my_list

def buble_sort(my_list):
    '''
    Сортировка методом пузырька.
    Суть сортировки заключается в том,
    Чтобы в диапозоне от 0 - N-1 сравнивать 2 соседних числа,
    Таким образом с каждым проходом большее число
    Будет "всплывать" в конец списка.
    :param my_list: list - не отсортированный список
    :return: my_list - отсортированный список
    '''

    last_item = len(my_list) - 1

    for bypass in range(1, last_item): # количество проходов
        for k in range(0, last_item-bypass):
            if my_list[k] > my_list[k+1]: # Сравнение двух элементов
                my_list[k], my_list[k+1] = my_list[k+1], my_list[k]

    return my_list

def test_sort(sort):
    '''
    Тестирует алгоритмы сортировки на выполнение своей задачи
    :my_list logic: list, несортированный список
    :return: отсортированный список my_list
    '''

    #TestCase1
    test_list = [7, 6, 5, 4, 3, 2, 1]
    test_list = sort(test_list)
    if test_list == [1, 2, 3, 4, 5, 6, 7]:
        print('#testCase1 - Okey')
    else:
        print('#testCase1 - Failed')

test_sort(buble_sort)
test_sort(choise_sort)
test_sort(insert_sort)