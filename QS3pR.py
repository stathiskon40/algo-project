from random import randint


def exchange(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def generatePivots(length):
    if length < 3:
        return 0, 0, 0
    p = randint(0, length-3)
    q = randint(p+1, length-2)
    r = randint(q+1, length-1)

    return p, q, r


def QuickSort3Pivot(list):
    global assignments, comparisons

    n = len(list)
    assignments += 1

    if n <= 1:
        comparisons += 1
        return list
    elif n == 2:
        comparisons += 2
        return sorted(list)

    comparisons += 2

    p, q, r = generatePivots(n)

    assignments += 3

    exchange(list, p, 0)
    exchange(list, q, 0)
    exchange(list, r, 0)

    assignments += 9

    pivot1, pivot2, pivot3 = sorted([list.pop(0), list.pop(0), list.pop(0)])
    assignments += 3

    a = []
    b = []
    c = []
    d = []

    for element in list:
        if element < pivot1:
            a.append(element)
            comparisons += 1
            assignments += 1
        elif pivot1 <= element < pivot2:
            b.append(element)
            comparisons += 3
            assignments += 1
        elif pivot2 <= element < pivot3:
            c.append(element)
            comparisons += 5
            assignments += 1
        else:
            d.append(element)
            comparisons += 5
            assignments += 1

    return QuickSort3Pivot(a) + [pivot1] + QuickSort3Pivot(b) + [pivot2] + QuickSort3Pivot(c) + [pivot3] + QuickSort3Pivot(d)


def QS3pR(array):
    global assignments, comparisons
    assignments, comparisons = 0, 0

    array = QuickSort3Pivot(array)

    return array, comparisons, assignments


# test = [99, 777, 44, 10, 89, 95, 14, 13, 444, 87, 12, 723, 2832, 2763, 72378]
# array, x1, x2 = QS3pR(test)
# print(array)
# print(comparisons, assignments)
# print(test, x1, x2)
