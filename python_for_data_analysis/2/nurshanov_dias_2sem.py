import numpy as np


def multiply_tuples(tup1: tuple, tup2: tuple):
    if len(tup1) < 2 or len(tup2) < 2:
        print('Both tuples must contain 2 elements.')
        return None
    numerator = tup1[0] * tup2[0]
    denominator = tup1[1] * tup2[1]
    return f'{numerator}/{denominator}'


def divide_tuples(tup1: tuple, tup2: tuple):
    if len(tup1) < 2 or len(tup2) < 2:
        print('Both tuples must contain 2 elements.')
        return None
    numerator = tup1[0] * tup2[1]
    denominator = tup1[1] * tup2[0]
    return f'{numerator}/{denominator}'


def get_smallest_fraction(fractions):
    return min(fractions, key=lambda frac: frac[0] / frac[1])


def exercise1():
    fraction1 = input('Enter the first fraction like (1/3, 52/1, and so on): ')
    fraction2 = input('Enter the second fraction like (1/3, 52/1, and so on): ')

    fraction1 = tuple(map(int, fraction1.split('/')))
    fraction2 = tuple(map(int, fraction2.split('/')))

    #Ex 1.1
    print('1.1 Exercise')
    print(f'Multiplication of the fractions: {multiply_tuples(fraction1, fraction2)}')
    print()
    #Ex 1.2
    print('1.2 Exercise')
    print(f'Division of the fractions: {divide_tuples(fraction1, fraction2)}')
    print()

    #Ex 1.3
    print('1.3 Exercise')
    fractions = []
    while True:
        fraction_input = input("Enter a fraction >>> ")

        if fraction_input.lower() == "stop":
            break

        try:
            num, den = map(int, fraction_input.split('/'))
            fractions.append((num, den))
        except ValueError:
            print("Please enter a valid fraction in the format numerator/denominator")

    if fractions:
        smallest_fraction = get_smallest_fraction(fractions)
        print(f"Smallest fraction: {smallest_fraction[0]}/{smallest_fraction[1]}")
    else:
        print("No fractions were entered.")


def exercise2():
    nums_all = []

    while True:
        value = input("Input a number >>> ")

        if value.lower() == "stop":
            break

        try:
            # Convert input to integer
            num = int(value)
            nums_all.append(num)
        except ValueError:
            print("Please enter a valid integer or 'stop' to finish.")

    # Convert the list to a NumPy array for easier manipulation
    nums_all_np = np.array(nums_all)

    # Split the numbers into even and odd
    nums_even_np = nums_all_np[nums_all_np % 2 == 0]
    nums_odd_np = nums_all_np[nums_all_np % 2 != 0]

    # Calculate sums and averages using NumPy
    sum_all = np.sum(nums_all_np)
    sum_even = np.sum(nums_even_np)
    sum_odd = np.sum(nums_odd_np)

    average_all = np.mean(nums_all_np) if nums_all_np.size > 0 else 0
    average_even = np.mean(nums_even_np) if nums_even_np.size > 0 else 0
    average_odd = np.mean(nums_odd_np) if nums_odd_np.size > 0 else 0

    # Print the results
    print(f"All numbers: {nums_all_np.tolist()}")
    print(f"Average of all numbers: {average_all}")
    print(f"Sum of all numbers: {sum_all}")

    print(f"Even numbers: {nums_even_np.tolist()}")
    print(f"Average of even numbers: {average_even}")
    print(f"Sum of even numbers: {sum_even}")

    print(f"Odd numbers: {nums_odd_np.tolist()}")
    print(f"Average of odd numbers: {average_odd}")
    print(f"Sum of odd numbers: {sum_odd}")
    print()


def insert_in_sorted_order(lst, num):
    if num in lst:
        return lst

    for i in range(len(lst)):
        if num < lst[i]:
            lst.insert(i, num)
            return lst

    lst.append(num)
    return lst


def exercise3():


    sorted_list = []

    while True:
        value = input("Input a number >>> ")

        if value.lower() == "stop":
            break

        try:
            num = float(value)
            sorted_list = insert_in_sorted_order(sorted_list, num)
        except ValueError:
            print("Please enter a valid number or 'stop' to finish.")


    print(sorted_list)


def option1(list: list):
    print()
    # Exercise 3 option 1 task 1
    print('Exercise 3 option 1 task 1')
    print(f'Number of positive items in list: {len([i for i in list if i > 0])}')

    print()
    # Exercise 3 option 1 task 2
    print('Exercise 3 option 1 task 2 ')
    print(f'The largest item in list - {max(list)}')
    print(f'The index of largest item in list - {list.index(max(list))}')

    print()
    # Exercise 3 option 1 task 3
    print('Exercise 3 option 1 task 3 ')
    odd_list = [i for i in list if i % 2 != 0]
    print('The smallest odd item in list', end=' ')
    if odd_list:
        print(min(odd_list))
    else:
        print(0)


def option2(list: list):
    print()
    # Exercise 3 option 2 task 1
    print('Exercise 3 option 2 task 1')
    ge_prev_item_list = []
    for i in range(1, len(list)):
        try:
            if list[i] > list[i - 1]:
                ge_prev_item_list.append(list[i])
        except IndexError:
            pass
    print(f'the list items that are larger than the previous item.', ge_prev_item_list)

    print()
    # Exercise 3 option 2 task 2
    print('Exercise 3 option 2 task 2 ')
    ge_neighbors_item_list = []
    for i in range(1, len(list) - 1):
        try:
            if list[i] > list[i - 1] and list[i] > list[i + 1]:
                ge_neighbors_item_list.append(list[i])
        except IndexError:
            pass
    print(f'number of elements in list that are greater than two of their neighbors', ge_neighbors_item_list)

    print()
    # Exercise 3 option 2 task 3
    print('Exercise 3 option 2 task 3 ')
    positive_list = [i for i in list if i > 0]
    smallest_positive = min(positive_list)
    print('smallest positive number', smallest_positive)


if __name__ == '__main__':
    exercise1()
    #Ex 2
    print()
    print('2 Exercise')
    exercise2()
    #Ex 3
    print()
    print('3 Exercise')
    exercise3()
    test_list =[12, -5, 0, 73, 45, -300, 100, -999, 8, 27]
    print(f'list for optiona a and b {test_list}')
    option1(test_list)
    option2(test_list)

zip()
