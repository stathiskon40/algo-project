def QS1pL_partition(array, low, high):
    i = (low+1)
    j = high
    pivot = array[low]

    comparisons = 0
    assignments = 3

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

        comparisons += 1
        assignments += 2
        array[i], array[j] = array[j], array[i]

    assignments += 2
    array[low], array[j] = array[j], array[low]

    return j, comparisons, assignments


# Function to perform quicksort
def QS1pLHelper(array, low, high):
    if low < high:

        pi, temp_comparisons, temp_assignments = QS1pL_partition(array, low, high)  # noqa

        global final_comparisons
        global final_assignments

        final_comparisons += temp_comparisons
        final_assignments += temp_assignments

        QS1pLHelper(array, low, pi - 1)
        QS1pLHelper(array, pi + 1, high)


def QS1pL(array):
    global final_comparisons
    global final_assignments

    final_comparisons, final_assignments = 0, 0

    QS1pLHelper(array, 0, len(array)-1)  # noqa

    return final_comparisons, final_assignments
