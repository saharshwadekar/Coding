import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = 'result_file.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Extract data from the DataFrame
array_sizes = data['Array Size']
bubble_sort_time = data['Bubble Sort Time']
selection_sort_time = data['Selection Sort Time']

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(array_sizes, bubble_sort_time, label='Bubble Sort Time', marker='o')
plt.plot(array_sizes, selection_sort_time, label='Selection Sort Time', marker='o')

plt.title('Sorting Algorithm Comparison')
plt.xlabel('Array Size')
plt.ylabel('Time (ms)')
plt.legend()
# plt.grid(True)
plt.show()