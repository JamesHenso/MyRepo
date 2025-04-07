import matplotlib.pyplot as plt
import numpy as np


algorithms = [
    "SelectionSort", "InsertionSort", "BubbleSort", "ShakerSort", "ShellSort",
    "HeapSort", "MergeSort", "QuickSort", "CountingSort", "RadixSort", "FlashSort"
]


data_sizes = [10, 100, 200, 500, 1000, 2000]


comparisons = {
    "SelectionSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "InsertionSort": [60, 5514, 21730, 130758, 519720, 1971110],
    "BubbleSort": [101, 10001, 40001, 250001, 1000001, 4000001],
    "ShakerSort": [95, 8403, 32607, 195247, 770563, 2971807],
    "ShellSort": [40, 872, 2333 , 6438, 15409, 37410],
    "HeapSort": [63, 1297, 3090, 9302, 21170, 47682],
    "MergeSort": [178, 3126, 7052, 20184, 44346, 96778],
    "QuickSort": [60, 1126, 2760, 7666, 15789, 35005],
    "CountingSort": [591414, 598538, 598938, 600138, 602138, 607986],
    "RadixSort": [432, 5224, 10890, 28584, 59276, 122963],
    "FlashSort": [91, 790, 1544, 3960, 7444, 15925]
}


comparison_values = np.array([comparisons[algo] for algo in algorithms])


bar_width = 0.12
x = np.arange(len(algorithms))


colors = ["#FFB5E8", "#B5EAD7", "#C7CEEA", "#FFDAC1", "#E2F0CB", "#B5D3E7"]

plt.figure(figsize=(18, 8))

for i, (size, color) in enumerate(zip(data_sizes, colors)):
    plt.bar(x + i * bar_width, comparison_values[:, i], width=bar_width, label=f"Size {size}", color=color)


plt.ylabel('Number of comparisons', fontsize=14, fontweight='bold')
plt.title('Randomized Data', fontsize=16, fontweight='bold')
plt.xticks(x + bar_width * (len(data_sizes) / 2 - 0.5), algorithms, rotation=30, ha='right', fontsize=12)
plt.legend(
    loc='upper center', 
    bbox_to_anchor=(0.5, -0.15), 
    ncol=len(data_sizes), 
    frameon=False
)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
