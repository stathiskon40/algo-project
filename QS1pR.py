from random import randint


def QS1pR_partition(array, low, high):
    i = (low+1)
    j = high

    assignments = 5
    comparisons = 0

    random_pivot = randint(low, high)

    array[random_pivot], array[low] = array[low], array[random_pivot]
    pivot = array[low]

    while 1:
        while array[i] <= pivot and i < high:
            i = i+1
            comparisons += 2
            assignments += 1

        comparisons += 2

        while array[j] > pivot and j > low:
            j = j-1
            comparisons += 2
            assignments += 1

        comparisons += 2

        if i >= j:
            comparisons += 1
            break

        comparisons += 1
        assignments += 2
        array[i], array[j] = array[j], array[i]

    assignments += 2
    array[low], array[j] = array[j], array[low]

    return j, comparisons, assignments

# Function to perform quicksort


def QS1pRHelper(array, low, high):
    if low < high:

        pi, temp_comparisons, temp_assignments = QS1pR_partition(
            array, low, high)

        global assignments
        global comparisons

        assignments += temp_assignments
        comparisons += temp_comparisons

        QS1pRHelper(array, low, pi - 1)
        QS1pRHelper(array, pi + 1, high)


def QS1pR(array):
    global comparisons, assignments

    comparisons = 0
    assignments = 0

    QS1pRHelper(array, 0, len(array)-1)

    return comparisons, assignments
