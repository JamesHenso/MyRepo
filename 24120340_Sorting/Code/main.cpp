#include <algorithm>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <fstream>

#include "BubbleSort.h"
#include "CountingSort.h"
#include "DataGenerator.h"
#include "FlashSort.h"
#include "HeapSort.h"
#include "InsertionSort.h"
#include "MergeSort.h"
#include "QuickSort.h"
#include "RadixSort.h"
#include "SelectionSort.h"
#include "ShakerSort.h"
#include "ShellSort.h"

using namespace std;
using namespace std::chrono;
typedef void (*sortAlgo)(int *, int, int &);

sortAlgo s[] = {selectionSort, insertionSort,
                bubbleSort, shakerSort, shellSort,
                heapSort, mergeSort, quickSort,
                countingSort, radixSort, flashSort};

const string algoName[11] = {
    "Selection", "Insertion", "Bubble", "Shaker", "Shell",
    "Heap", "Merge", "Quick", "Counting", "Radix", "Flash"}; // string sort

const string dataDistribution[4] = {"RandomData", "SortedData", "ReverseData",
                                    "NearlySortedData"};

const int dataSize[4] = {10000, 30000, 50000, 100000};

double process(int *a, int n, sortAlgo f, int nameIdx, int &counting) // process time
{
    counting = 0; // Reset counting before sorting
    auto start = system_clock::now();
    f(a, n, counting);
    auto stop = system_clock::now();
    std::chrono::duration<double, std::milli> timeCost = stop - start;
    double ms = timeCost.count();
    cout << setw(25) << left << (algoName[nameIdx] + "Sort: ") << setw(25)
         << right << fixed << setprecision(3) << ms << " ms\t->";
    if (is_sorted(a, a + n))
        cout << "SUCCEED! Comparisons: " << counting << "\n";
    else
        cout << "NOOOOOO!\n";
    return ms;
}

bool validAlgo(const string &algo)
{
    for (int i = 0; i < 11; i++)
    {
        if (algoName[i] == algo)
            return true;
    }
    return false;
}

int main(int argc, char *argv[])
{
    int *source = NULL;
    int *a = NULL;

    for (int t = 0; t < 4; ++t)
    {
        cout << dataDistribution[t] << "\n";
        for (int sz = 0; sz < 4; ++sz)
        {
            int n = dataSize[sz];
            cout << "Data Size = " << n << "\n";

            double time = 0;
            int counting = 0; // Variable to store the number of comparisons

            // Generate integer array
            source = new int[n];
            generateData(source, n, t);

            // Sort array and show the time cost
            for (int algo = 0; algo < 11; ++algo)
            {
                restoreArray(source, a, n);
                time = process(a, n, s[algo], algo, counting);
            }

            delete[] source;
            cout << "\n";
        }

        cout << "*************************************\n\n";
    }

    // Chose the way to sort array

    if (argc != 7)
    {
        cout << "./main.ext -a <Sort_way> -i <input_txt> -o <output_txt>"; // Lỗi đầu vào
        return 0;
    }

    string sort_way, input_file, output_file;

    for (int i = 1; i < argc; i += 2)
    {
        if (strcmp(argv[i], "-a") == 0)
        {
            sort_way = argv[i + 1];
            if (!validAlgo(sort_way))
            {
                cout << "Invalid sorting algorithm.";
                return 0;
            }
        }
        else if (strcmp(argv[i], "-i") == 0)
        {
            input_file = argv[i + 1];
        }
        else if (strcmp(argv[i], "-o") == 0)
        {
            output_file = argv[i + 1];
        }
        else
        {
            cout << "Invalid argument: " << argv[i];
            return 0;
        }
    }

    ifstream file(input_file);
    if (!file)
    {
        cout << "Invalid file.";
    }
    int num;
    file >> num; // lấy n phần tử
    int *arr = new int[num];
    for (int i = 0; i < num; i++)
    {
        file >> arr[i]; // lấy giá trị phần tử
    }
    file.close();

    auto it = find(begin(algoName), end(algoName), sort_way);
    if (it != end(algoName))
    {
        int idx = distance(begin(algoName), it); // lấy index
        int counting = 0;                        // Variable to store the number of comparisons
        s[idx](arr, num, counting);              // thực hiện sort
        cout << "Comparisons: " << counting << "\n";
    }
    else
    {
        cout << "Invalid sorting algorithm specified.";
        delete[] arr;
        return 0;
    }

    ofstream output(output_file);
    if (!output)
    {
        cout << "Unable to open output file.";
        delete[] arr;
        return 0;
    }
    output << num << endl;
    for (int i = 0; i < num; i++)
    {
        output << arr[i] << " "; // output ra file
    }
    output.close();
    delete[] arr;
    return 0;
}