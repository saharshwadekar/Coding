import pandas as pd
import matplotlib.pyplot as plt

def microToSeconds(microsecond):
    return microsecond / 1000000

# Read the CSV file
heap_file_path = '/Users/saharsh/Documents/Coding/Data Analysis And Algorithm/3_Practical/heapSort.csv'
quick_file_path = '/Users/saharsh/Documents/Coding/Data Analysis And Algorithm/3_Practical/quickSort.csv'

bdata = pd.read_csv(heap_file_path)
sdata = pd.read_csv(quick_file_path)

# Extract data from the DataFrame
array_sizes = bdata['Array Size']
heap_sort_time = bdata['Time (Heap Sort)']
heap_sort_time = list(map(microToSeconds,heap_sort_time))

quick_sort_time = sdata['Time (Quick Sort)']
quick_sort_time = list(map(microToSeconds,quick_sort_time))

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(array_sizes, heap_sort_time, label='heap Sort Time', marker='o')
plt.plot(array_sizes, quick_sort_time, label='quick Sort Time', marker='o')

plt.title('Sorting Algorithm Comparison')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()

plt.show()