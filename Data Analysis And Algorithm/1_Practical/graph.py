import pandas as pd
import matplotlib.pyplot as plt

def microToSeconds(microsecond):
    return microsecond / 1000000

# Read the CSV file
bubble_file_path = 'bubbleSort.csv' 
selection_file_path = 'selectionSort.csv'

bdata = pd.read_csv(bubble_file_path)
sdata = pd.read_csv(selection_file_path)

# Extract data from the DataFrame
array_sizes = bdata['Array Size']
bubble_sort_time = bdata['Time (Bubble Sort)']
bubble_sort_time = list(map(microToSeconds,bubble_sort_time))

selection_sort_time = sdata['Time (Selection Sort)']
selection_sort_time = list(map(microToSeconds,selection_sort_time))

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(array_sizes, bubble_sort_time, label='Bubble Sort Time', marker='o')
plt.plot(array_sizes, selection_sort_time, label='Selection Sort Time', marker='o')

plt.title('Sorting Algorithm Comparison')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
# plt.grid(True)
plt.show()