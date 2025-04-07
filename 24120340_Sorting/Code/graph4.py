import matplotlib.pyplot as plt

input_sizes = [10, 100, 200, 500, 1000, 2000]

data = {
 
    "SelectionSort":       [0.001, 0.010, 0.040, 0.102, 0.414, 3.167],
    "InsertionSort":       [0.001, 0.002, 0.003, 0.005, 0.009, 0.018],
    "BinaryInsertionSort": [0.001, 0.004, 0.006, 0.014, 0.031, 0.090],
    "BubbleSort":          [0.001, 0.008, 0.041, 0.116, 0.890, 2.085],
    "ShakerSort":          [0.001, 0.004, 0.005, 0.013, 0.029, 0.060],
    "ShellSort":           [0.001, 0.006, 0.006, 0.016, 0.034, 0.066],
    "HeapSort":            [0.002, 0.008, 0.011, 0.036, 0.079, 0.135],
    "MergeSort":           [0.003, 0.024, 0.024, 0.101, 0.103, 0.229],
    "QuickSort":           [0.003, 0.004, 0.004, 0.009, 0.016, 0.029],
    "CountingSort":        [0.001, 0.002, 0.003, 0.006, 0.014, 0.019],
    "RadixSort":           [0.002, 0.004, 0.006, 0.014, 0.037, 0.044],
    "FlashSort":           [0.001, 0.004, 0.009, 0.012, 0.022, 0.038]
}




markers = ['o', 's', '^', 'v', 'D', 'x', '+', '1', '*', 'p', 'h']
colors = [
    'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black',
    '#FFA500', '#8A2BE2', '#00CED1', '#FF69B4'
]

plt.figure(figsize=(14, 8))
for (algo, runtimes), marker, color in zip(data.items(), markers, colors):
    plt.plot(input_sizes, runtimes, marker=marker, color=color, label=algo)


plt.grid(False)


plt.grid(axis='y', color='gray', alpha=0.5)


for x in input_sizes:
    plt.axvline(x=x, color='gray', linestyle='--', linewidth=1)

plt.title(
'Nearly Sorted Data', fontsize=16, fontweight='bold')
plt.xlabel('Input Size', fontsize=12, fontweight='bold')
plt.ylabel('Run Time (ms)', fontsize=12, fontweight='bold')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
plt.tight_layout()
plt.show()
