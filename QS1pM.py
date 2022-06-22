from random import randint


def median_pivot(low, high):
    cand_pivot_1 = randint(low, high)
    cand_pivot_2 = randint(low, high)

    assignments = 2
    comparisons = 0

    # Generate the second pivot and check if the pivot is greater than 2
    while cand_pivot_1 == cand_pivot_2 and high-low > 1:
        cand_pivot_2 = randint(low, high)
        comparisons += 2
        assignments += 1

    comparisons += 2

    cand_pivot_3 = randint(low, high)
    assignments += 1

    # Generate third pivot and check if the size of the array is bigger than three
    while cand_pivot_3 == cand_pivot_2 or cand_pivot_3 == cand_pivot_1 and high-low > 2:
        cand_pivot_3 = randint(low, high)
        comparisons += 3
        assignments += 1

    comparisons += 3

    final_pivot = int((cand_pivot_1+cand_pivot_2+cand_pivot_3)/3)
    assignments += 1

    return final_pivot, comparisons, assignments


def QS1pM_partition(array, low, high):
    i = (low+1)
    j = high

    final_pivot, comparisons, assignments = median_pivot(low, high)

    assignments = +2

    array[final_pivot], array[low] = array[low], array[final_pivot]
    pivot = array[low]

    assignments += 2

    while 1:
        while array[i] <= pivot and i < high:
            i = i+1
            assignments += 1
            comparisons += 2

        comparisons += 2

        while array[j] > pivot and j > low:
            j = j-1
            assignments += 1
            comparisons += 2

        comparisons += 2

        if i >= j:
            comparisons += 1
            break

        array[i], array[j] = array[j], array[i]
        comparisons += 1
        assignments += 2

    array[low], array[j] = array[j], array[low]
    assignments += 2

    return j, comparisons, assignments


def QS1pMHelper(array, low, high):
    if low < high:

        pi, temp_comparisons, temp_assignments = QS1pM_partition(array, low, high)  # noqa

        global comparisons
        global assignments

        comparisons += temp_comparisons
        assignments += temp_assignments

        QS1pMHelper(array, low, pi - 1)
        QS1pMHelper(array, pi + 1, high)


def QS1pM(array):
    global comparisons
    global assignments

    comparisons = 0
    assignments = 0

    QS1pMHelper(array, 0, len(array)-1)

    return comparisons, assignments
