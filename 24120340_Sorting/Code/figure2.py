import matplotlib.pyplot as plt

input_sizes = [10, 100, 200, 500, 1000, 2000]

data = {
    "SelectionSort":   [0.000, 0.044, 0.035, 0.127, 0.719, 1.592],
"InsertionSort":   [0.000, 0.000, 0.003, 0.002, 0.003, 0.003],
"BubbleSort":      [0.000, 0.009, 0.017, 0.184, 0.386, 1.558],
"ShakerSort":      [0.000, 0.000, 0.002, 0.001, 0.005, 0.002],
"ShellSort":       [0.000, 0.001, 0.004, 0.012, 0.012, 0.029],
"HeapSort":        [0.001, 0.006, 0.012, 0.032, 0.262, 0.157],
"MergeSort":       [0.002, 0.052, 0.025, 0.061, 0.124, 0.638],
"QuickSort":       [0.002, 0.003, 0.003, 0.019, 0.012, 0.028],
"CountingSort":    [0.001, 0.003, 0.007, 0.022, 0.013, 0.049],
"RadixSort":       [0.001, 0.003, 0.005, 0.018, 0.023, 0.048],
"FlashSort":       [0.002, 0.005, 0.020, 0.011, 0.074, 0.037]

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
'Sorted Data', fontsize=16, fontweight='bold')
plt.xlabel('Input Size', fontsize=12, fontweight='bold')
plt.ylabel('Run Time (ms)', fontsize=12, fontweight='bold')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
plt.tight_layout()
plt.show()
