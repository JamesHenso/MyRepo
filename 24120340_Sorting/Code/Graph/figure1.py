import matplotlib.pyplot as plt

input_sizes = [10, 100, 200, 500, 1000, 2000]

data = {
    "SelectionSort":      [0.001, 0.009, 0.035, 0.126, 0.453, 1.892],
    "InsertionSort":      [0.000, 0.004, 0.013, 0.066, 0.494, 1.895],
    "BubbleSort":         [0.001, 0.021, 0.074, 0.396, 1.467, 5.897],
    "ShakerSort":         [0.003, 0.018, 0.065, 0.398, 1.598, 5.625],
    "ShellSort":          [0.001, 0.016, 0.011, 0.035, 0.107, 0.180],
    "HeapSort":           [0.003, 0.006, 0.017, 0.035, 0.121, 0.174],
    "MergeSort":          [0.011, 0.114, 0.031, 0.075, 0.155, 0.511],
    "QuickSort":          [0.002, 0.005, 0.014, 0.035, 0.073, 0.158],
    "CountingSort":       [0.760, 0.860, 1.186, 0.837, 1.596, 1.009],
    "RadixSort":          [0.002, 0.012, 0.026, 0.068, 0.133, 0.262],
    "FlashSort":          [0.011, 0.004, 0.017, 0.024, 0.116, 0.051]
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

plt.title('Randomized Data', fontsize=16, fontweight='bold')
plt.xlabel('Input Size', fontsize=12, fontweight='bold')
plt.ylabel('Run Time (ms)', fontsize=12, fontweight='bold')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
plt.tight_layout()
plt.show()
