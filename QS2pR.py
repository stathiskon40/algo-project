import random


def exchange(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def QuickSort2Pivot(list):
    global comparisons
    global assignments

    n = len(list)
    assignments += 1

    if n <= 1:
        comparisons += 1
        return list
    elif n == 2:
        comparisons += 3
        assignments += 2
        return sorted(list)

    comparisons += 2

    random_pivot_1 = random.randint(0, n-1)
    random_pivot_2 = random.randint(0, n-1)

    while(random_pivot_1 == random_pivot_2):
        comparisons += 1
        assignments += 1
        random_pivot_2 = random.randint(0, n-1)

    comparisons += 1

    exchange(list, random_pivot_1, 0)
    exchange(list, random_pivot_2, 1)

    assignments += 6

    pivot1, pivot2 = sorted([list.pop(0), list.pop(0)])

    comparisons += 2
    assignments += 2

    a = []
    b = []
    c = []
    for element in list:
        if element < pivot1:
            comparisons += 1
            assignments += 1
            a.append(element)
        elif pivot1 <= element < pivot2:
            comparisons += 3
            assignments += 1
            b.append(element)
        else:
            comparisons += 3
            assignments += 1
            c.append(element)

    return QuickSort2Pivot(a) + [pivot1] + QuickSort2Pivot(b) + [pivot2] + QuickSort2Pivot(c)


def QS2pR(array):
    global comparisons
    global assignments

    comparisons = 0
    assignments = 0

    array = QuickSort2Pivot(array)

    return array, comparisons, assignments
