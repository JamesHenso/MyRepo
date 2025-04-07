import matplotlib.pyplot as plt

input_sizes = [10, 100, 200, 500, 1000, 2000]

data = {
    "SelectionSort":   [0.000, 0.006, 0.020, 0.128, 0.665, 2.389],
"InsertionSort":   [0.002, 0.012, 0.022, 0.140, 1.150, 2.088],
"BubbleSort":      [0.000, 0.051, 0.105, 0.447, 1.808, 7.399],
"ShakerSort":      [0.001, 0.026, 0.071, 0.559, 1.768, 7.142],
"ShellSort":       [0.001, 0.012, 0.011, 0.017, 0.021, 0.048],
"HeapSort":        [0.001, 0.021, 0.024, 0.027, 0.074, 0.129],
"MergeSort":       [0.002, 0.028, 0.033, 0.059, 0.115, 0.214],
"QuickSort":       [0.000, 0.002, 0.003, 0.019, 0.013, 0.027],
"CountingSort":    [0.001, 0.002, 0.009, 0.020, 0.020, 0.126],
"RadixSort":       [0.005, 0.005, 0.009, 0.025, 0.035, 0.052],
"FlashSort":       [0.005, 0.004, 0.005, 0.010, 0.033, 0.044]


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

plt.title('R' \
'Reverse Sorted Data', fontsize=16, fontweight='bold')
plt.xlabel('Input Size', fontsize=12, fontweight='bold')
plt.ylabel('Run Time (ms)', fontsize=12, fontweight='bold')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
plt.tight_layout()
plt.show()
