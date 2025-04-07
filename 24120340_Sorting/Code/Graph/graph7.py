import matplotlib.pyplot as plt
import numpy as np


algorithms = [
    "SelectionSort", "InsertionSort", "BubbleSort", "ShakerSort", "ShellSort",
    "HeapSort", "MergeSort", "QuickSort", "CountingSort", "RadixSort", "FlashSort"
]


data_sizes = [10, 100, 200, 500, 1000, 2000]


comparisons = {

    "SelectionSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "InsertionSort": [102, 10002, 40002, 250002, 1000002, 4000002],
    "BubbleSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "ShakerSort": [103, 10003, 40003, 250003, 1000003, 4000003],
    "ShellSort": [39, 770, 1831, 5615, 12716, 28417],
    "HeapSort": [44, 1130, 2705, 8413, 19159, 43495],
    "MergeSort": [170, 2750, 6106, 17014, 37034, 80074],
    "QuickSort": [61, 861, 1919, 5033, 11059, 24109],
    "CountingSort": [64, 604, 1204, 3004, 6004, 12004],
    "RadixSort": [249, 3250, 7072, 19258, 41496, 88972],
    "FlashSort": [84, 764, 1521, 3790, 7573, 15138]
}




comparison_values = np.array([comparisons[algo] for algo in algorithms])


bar_width = 0.12
x = np.arange(len(algorithms)) *1.5


colors = ["#FFB5E8", "#B5EAD7", "#C7CEEA", "#FFDAC1", "#E2F0CB", "#B5D3E7"]

plt.figure(figsize=(18, 8))

for i, (size, color) in enumerate(zip(data_sizes, colors)):
    plt.bar(x + i * bar_width, comparison_values[:, i], width=bar_width, label=f"Size {size}", color=color)


plt.ylabel('Number of comparisons', fontsize=14, fontweight='bold')
plt.title('Reverse Sorted Data', fontsize=16, fontweight='bold')
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
