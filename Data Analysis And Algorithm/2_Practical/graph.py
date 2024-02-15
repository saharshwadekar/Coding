import pandas as pd
import matplotlib.pyplot as plt

def microToSeconds(microsecond):
    return microsecond / 1000000

# Read the CSV file
insertion_file_path = 'insertionSort.csv'
merge_file_path = 'mergeSort.csv'

bdata = pd.read_csv(insertion_file_path)
sdata = pd.read_csv(merge_file_path)

# Extract data from the DataFrame
array_sizes = bdata['Array Size']
insertion_sort_time = bdata['Time (Insertion Sort)']
insertion_sort_time = list(map(microToSeconds,insertion_sort_time))

merge_sort_time = sdata['Time (Merge Sort)']
merge_sort_time = list(map(microToSeconds,merge_sort_time))

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(array_sizes, insertion_sort_time, label='Insertion Sort Time', marker='o')
plt.plot(array_sizes, merge_sort_time, label='Merge Sort Time', marker='o')

plt.title('Sorting Algorithm Comparison')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
# plt.grid(True)
plt.show()