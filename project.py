from asyncore import read
from cgi import test
from alive_progress import alive_bar
import time
import random
import sys
import csv
import os
##################
from QS1pL import QS1pL
from QS1pR import QS1pR
from QS1pM import QS1pM
from QS2pR import QS2pR
from QS3pR import QS3pR
from QS2pRPre import QS2pRPre
from QS3pRPre import QS3pRPre

sys.setrecursionlimit(2**29)


def mean(array):
    sum = 0
    for i in array:
        sum += i

    return sum/len(array)


def variance(array):
    squared_array = []
    for i in array:
        squared_array.append(i**2)

    array_mean = mean(array)**2
    squared_array_mean = mean(squared_array)

    return squared_array_mean - array_mean


def generateArray(array, size):
    for _ in range(0, size):
        array.append(random.randint(1, 2*size))

    return array


testing_array = []
error = False
selected_method_of_sorting = 0

array_sizes = [10000, 100000, 1000000, 10000000]
methods = ["QS1pL", "QS1pM", "QS1pR", "QS2pR", "QS3pR", "QS2pRPre", "QS3pRPre"]

time_results = []
assignments_results = []
comparisons_results = []

mean_file = open("mean_variance.txt", "wt")

csv_file = open("times.csv", 'w', newline='')
the_writer = csv.writer(csv_file)

for size in array_sizes:
    for selected_method_of_sorting in range(0, 7):
        print(f"\nCurrect size sorting: {size}")
        print(f"Current method of sorting: {methods[selected_method_of_sorting]}")  # noqa
        with alive_bar(50) as bar:
            for _ in range(1, 51):
                testing_array = generateArray(testing_array, size)

                if(selected_method_of_sorting == 0):
                    t_start = time.perf_counter()
                    temp_comparisons, temp_assignments = QS1pL(testing_array)  # noqa
                    time_results.append(time.perf_counter() - t_start)
                    assignments_results.append(temp_assignments)
                    comparisons_results.append(temp_comparisons)
                elif(selected_method_of_sorting == 1):
                    t_start = time.perf_counter()
                    temp_comparisons, temp_assignments = QS1pM(testing_array)  # noqa
                    time_results.append(time.perf_counter() - t_start)
                    assignments_results.append(temp_assignments)
                    comparisons_results.append(temp_comparisons)
                elif(selected_method_of_sorting == 2):
                    t_start = time.perf_counter()
                    temp_comparisons, temp_assignments = QS1pR(testing_array)  # noqa
                    time_results.append(time.perf_counter() - t_start)
                    assignments_results.append(temp_assignments)
                    comparisons_results.append(temp_comparisons)
                elif(selected_method_of_sorting == 3):
                    t_start = time.perf_counter()
                    testing_array, temp_comparisons, temp_assignments = QS2pR(testing_array)  # noqa
                    time_results.append(time.perf_counter() - t_start)
                    assignments_results.append(temp_assignments)
                    comparisons_results.append(temp_comparisons)
                elif(selected_method_of_sorting == 4):
                    t_start = time.perf_counter()
                    testing_array, temp_comparisons, temp_assignments = QS3pR(testing_array)  # noqa
                    time_results.append(time.perf_counter() - t_start)
                    assignments_results.append(temp_assignments)
                    comparisons_results.append(temp_comparisons)
                elif(selected_method_of_sorting == 5):
                    t_start = time.perf_counter()
                    testing_array, temp_comparisons, temp_assignments = QS2pRPre(testing_array)  # noqa
                    time_results.append(time.perf_counter() - t_start)
                    assignments_results.append(temp_assignments)
                    comparisons_results.append(temp_comparisons)
                elif(selected_method_of_sorting == 6):
                    t_start = time.perf_counter()
                    testing_array, temp_comparisons, temp_assignments = QS3pRPre(testing_array)  # noqa
                    time_results.append(time.perf_counter() - t_start)
                    assignments_results.append(temp_assignments)
                    comparisons_results.append(temp_comparisons)
                bar()
                testing_array.clear()

        # Here goes the txt file
        # MEAN
        array_mean_assignments = mean(assignments_results)
        array_mean_comparisons = mean(comparisons_results)
        array_mean_times = mean(time_results)

        # VARIANCE
        array_variance_assignments = variance(assignments_results)
        array_variance_comparisons = variance(comparisons_results)
        array_variance_times = variance(time_results)

        mean_file.write(
            f"Current method of sorting:{methods[selected_method_of_sorting]}\n")
        mean_file.write(f"Current size:{size}\n\n")
        mean_file.write(f"Assignments mean: {array_mean_assignments}\n")
        mean_file.write(f"Comparisons mean: {array_mean_comparisons}\n")
        mean_file.write(f"Times mean: {array_mean_times}\n\n")

        mean_file.write(
            f"Assignments variance: {array_variance_assignments}\n")
        mean_file.write(
            f"Comparisons variance: {array_variance_comparisons}\n")
        mean_file.write(
            f"Times variance: {array_variance_times}\n\n")
        mean_file.write("\n--------------------------------------------\n")

        ####
        # Here goes the txt file
        the_writer.writerow(
            ["Method:" + methods[selected_method_of_sorting], 'Times', 'Comparisons', 'Size: ' + str(size)])
        for i in range(0, len(assignments_results)):
            the_writer.writerow(
                ['', time_results[i], assignments_results[i], ''])

        time_results.clear()
        assignments_results.clear()
        assignments_results.clear()

csv_file.close()

with open('times.csv', 'r') as times_file:
    with open('final.csv', 'w') as final_file:
        reader = csv.reader(times_file)
        writer = csv.writer(final_file)

        reader = list(reader)

        current_row = []
        space = []
        index = 0
        helping_index = 0
        new_index = 0

        for j in range(0, len(array_sizes)):
            for i in range(0, 51):
                index = helping_index + new_index
                for k in range(0, len(methods)):

                    current_row += reader[index]
                    current_row += ['']
                    index += 51

                writer.writerow(current_row)
                current_row.clear()
                helping_index += 1

            for i in range(0, 34):
                space += ['']

            writer.writerow(space)

            new_index = index - 50
            helping_index = 0

os.remove("times.csv")

print("---Program finished successfuly---")
