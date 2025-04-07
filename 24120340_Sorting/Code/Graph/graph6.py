import matplotlib.pyplot as plt
import numpy as np


algorithms = [
    "SelectionSort", "InsertionSort", "BubbleSort", "ShakerSort", "ShellSort",
    "HeapSort", "MergeSort", "QuickSort", "CountingSort", "RadixSort", "FlashSort"
]


data_sizes = [10, 100, 200, 500, 1000, 2000]


comparisons = {
    
    "SelectionSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "InsertionSort": [12, 102, 202, 502, 1002, 2002],
    "BubbleSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "ShakerSort": [23, 203, 403, 1003, 2003, 4003],
    "ShellSort": [26, 510, 1211, 3515, 8016, 18017],
    "HeapSort": [66, 1488, 3486, 10319, 23174, 51153],
    "MergeSort": [162, 2670, 5946, 16902, 36810, 79626],
    "QuickSort": [54, 857, 1914, 5027, 11052, 24101],
    "CountingSort": [64, 604, 1204, 3004, 6004, 12004],
    "RadixSort": [244, 3200, 6972, 19008, 40996, 87972],
    "FlashSort": [90, 861, 1718, 4289, 8574, 17144]

}


comparison_values = np.array([comparisons[algo] for algo in algorithms])


bar_width = 0.12
x = np.arange(len(algorithms)) *1.5


colors = ["#FFB5E8", "#B5EAD7", "#C7CEEA", "#FFDAC1", "#E2F0CB", "#B5D3E7"]

plt.figure(figsize=(18, 8))

for i, (size, color) in enumerate(zip(data_sizes, colors)):
    plt.bar(x + i * bar_width, comparison_values[:, i], width=bar_width, label=f"Size {size}", color=color)


plt.ylabel('Number of comparisons', fontsize=14, fontweight='bold')
plt.title('Sorted Data', fontsize=16, fontweight='bold')
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
