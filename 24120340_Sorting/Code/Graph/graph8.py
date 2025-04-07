import matplotlib.pyplot as plt
import numpy as np


algorithms = [
    "SelectionSort", "InsertionSort", "BubbleSort", "ShakerSort", "ShellSort",
    "HeapSort", "MergeSort", "QuickSort", "CountingSort", "RadixSort", "FlashSort"
]


data_sizes = [10, 100, 200, 500, 1000, 2000]


comparisons = {

    "SelectionSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "InsertionSort": [38, 1162, 2606, 4898, 10186, 25894],
    "BubbleSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "ShakerSort": [79, 2435, 5035, 10883, 17923, 51835],
    "ShellSort": [31, 786, 1677, 4405, 9472, 22155],
    "HeapSort": [60, 1450, 3405, 10249, 23138, 51391],
    "MergeSort": [180, 2972, 6446, 18350, 39456, 86658],
    "QuickSort": [75, 898, 1940, 5038, 11052, 24101],
    "CountingSort": [64, 604, 1204, 3004, 6004, 12004],
    "RadixSort": [249, 3218, 6994, 19022, 41008, 87992],
    "FlashSort": [87, 847, 1705, 4273, 8556, 17128]
}




comparison_values = np.array([comparisons[algo] for algo in algorithms])


bar_width = 0.12
x = np.arange(len(algorithms)) *1.5


colors = ["#FFB5E8", "#B5EAD7", "#C7CEEA", "#FFDAC1", "#E2F0CB", "#B5D3E7"]

plt.figure(figsize=(18, 8))

for i, (size, color) in enumerate(zip(data_sizes, colors)):
    plt.bar(x + i * bar_width, comparison_values[:, i], width=bar_width, label=f"Size {size}", color=color)


plt.ylabel('Number of comparisons', fontsize=14, fontweight='bold')
plt.title('Nearly Sorted Data', fontsize=16, fontweight='bold')
plt.xticks(x + bar_width * (len(data_sizes) / 2 - 0.5), algorithms, rotation=0, ha='center', fontsize=12)
plt.legend(
    loc='upper center', 
    bbox_to_anchor=(0.5, -0.15), 
    ncol=len(data_sizes), 
    frameon=False
)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
