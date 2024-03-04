import pandas as pd
import matplotlib.pyplot as plt

def microToSeconds(microsecond):
    return microsecond / 1000000

# Read the CSV file
insertion_file_path = 'insertionSort.csv'
merge_file_path = 'mergeSort.csv'

# bdata = pd.read_csv(insertion_file_path)
# sdata = pd.read_csv(merge_file_path)

# Extract data from the DataFrame
array_sizes = [500,1000,1500,2000,2500,3000]
# insertion_sort_time = bdata['Time (Insertion Sort)']
insertion_sort_time = [0.001524,0.002621,0.009897,0.007993,0.012003 ,0.016805]

insertion_sort_time = list(map(microToSeconds,insertion_sort_time))

# merge_sort_time = sdata['Time (Merge Sort)']
merge_sort_time = [0.744344,2.40992,5.04358,8.70643,13.3765,19.0755]
merge_sort_time = list(map(microToSeconds,merge_sort_time))

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(array_sizes, insertion_sort_time, label='Merge Sort Time', marker='o')
plt.plot(array_sizes, merge_sort_time, label='Insertion Sort Time', marker='o')

plt.title('Sorting Algorithm Comparison')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
# plt.grid(True)
plt.show()