from random import randint
from math import sqrt
from QS3pR import QS3pR

pivots_in_final_array = []


def selectPivots(array):
    global assignments, comparisons

    number_of_pivots = int(sqrt(len(array)))
    pivots = []

    assignments += 1

    start = 0
    size_of_subarrays = int(len(array)/number_of_pivots)

    assignments += 2

    for i in range(0, number_of_pivots):
        assignments += 1

        finish = ((i+1)*size_of_subarrays)-1
        assignments += 1

        pivot = randint(start, finish)
        assignments += 1

        start = finish+1
        assignments += 1

        pivots.append(pivot)
        assignments += 1

    return pivots


def quickSortSpecificPivot(array, start, finish, pivots):
    global assignments, comparisons
    pivot_index = pivots.pop(0)
    pivot_value = array[pivot_index]

    assignments += 2

    try:
        renew_pivot = pivots.index(finish)
        pivots[renew_pivot] = pivot_index
    except:
        pass

    comparisons += len(pivots)

    array[finish], array[pivot_index] = array[pivot_index], array[finish]
    assignments += 2

    i, j = start, finish-1
    assignments += 2

    while 1:

        while array[i] <= pivot_value and i < finish:
            i = i+1
            comparisons += 2
            assignments += 1

        comparisons += 2

        while array[j] > pivot_value and j > start:
            j = j-1
            comparisons += 2
            assignments += 1

        comparisons += 2

        if i >= j:
            comparisons += 1
            break

        comparisons += 1

        try:
            renew_pivot = pivots.index(i)
            pivots[renew_pivot] = j
            assignments += 1
        except:
            pass

        try:
            renew_pivot = pivots.index(j)
            pivots[renew_pivot] = i
            assignments += 1
        except:
            pass

        comparisons += 2*len(pivots)

        array[i], array[j] = array[j], array[i]
        assignments += 2

    array[i], array[finish] = array[finish], array[i]
    assignments += 2

    try:
        renew_pivot = pivots.index(finish)
        pivots[renew_pivot] = j
        assignments += 1
    except:
        pass

    try:
        renew_pivot = pivots.index(i)
        pivots[renew_pivot] = finish
        assignments += 1
    except:
        pass

    comparisons += 2*len(pivots)

    if(len(pivots)):
        old = pivots[0]
        assignments += 1

        min_pivot = min(pivots)
        index = pivots.index(min_pivot)

        comparisons += len(pivots)

        pivots[0] = min_pivot
        pivots[index] = old
        assignments += 2

    return i


def preSorting(array, start, finish, pivots):
    global comparisons, assignments
    if start <= finish:
        comparisons += 1
        pi = quickSortSpecificPivot(array, start, finish, pivots)
        pivots_in_final_array.append(pi)
        assignments += 1

        while len(pivots) and pivots[0] <= finish and pivots[0] >= start:
            comparisons += 3
            while len(pivots) > 0 and pivots[0] > pi and pivots[0] <= finish:
                preSorting(array, pi+1, finish, pivots)
                comparisons += 3

            while len(pivots) > 0 and pivots[0] < pi and pivots[0] >= start:
                preSorting(array, start, pi-1, pivots)
                comparisons += 3


def QS3pRPre(array):
    global comparisons, assignments
    comparisons = 0
    assignments = 0

    pivots = selectPivots(array)

    start = 0
    finish = len(array)-1

    assignments += 3
    preSorting(array, start, finish, pivots)

    start = 0
    try:
        pivots_in_final_array.remove(start)
    except:
        pass

    comparisons += len(pivots_in_final_array)

    finish = min(pivots_in_final_array)
    pivots_in_final_array.remove(finish)

    comparisons += len(pivots_in_final_array)

    while(len(pivots_in_final_array)):
        array[start:finish], temp_comparisons, temp_asignments = QS3pR(
            array[start:finish])

        comparisons += temp_comparisons
        assignments += temp_asignments

        start = finish+1
        assignments += 1

        if len(pivots_in_final_array):
            comparisons += 1
            finish = min(pivots_in_final_array)
            pivots_in_final_array.remove(finish)
            comparisons += len(pivots_in_final_array)

    array[start:finish], temp_comparisons, temp_asignments = QS3pR(
        array[start:finish])

    comparisons += temp_comparisons
    assignments += temp_asignments

    start = finish
    finish = len(array)
    assignments += 2

    array[start:finish], temp_comparisons, temp_asignments = QS3pR(
        array[start:finish])

    comparisons += temp_comparisons
    assignments += temp_asignments

    return array, comparisons, assignments
