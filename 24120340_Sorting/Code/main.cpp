#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <sstream>

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

typedef void (*sortAlgo)(int *, int);

sortAlgo s[] = {selectionSort, insertionSort,
                bubbleSort, shakerSort, shellSort,
                heapSort, mergeSort, quickSort,
                countingSort, radixSort, flashSort};

const string algoName[11] = {
    "selection", "insertion", "bubble", "shaker", "shell",
    "heap", "merge", "quick", "counting", "radix", "flash"}; // string sort

bool validAlgo(const string &algo)
{
    return find(begin(algoName), end(algoName), algo) != end(algoName);
}

int main(int argc, char *argv[])
{

    // Chose the way to sort array

    if (argc != 7)
    {
        cout << "./main.ext -a <sort_way> -i <input_txt> -o <output_txt>"; // Lỗi đầu vào
        return 0;
    }

    string sort_way, input_file, output_file;

    for (int i = 1; i < argc; i += 2)
    {
        if (strcmp(argv[i], "-a") == 0)
        {
            string get_str = argv[i + 1];
            size_t pos = get_str.find('-');
            sort_way = (pos != string::npos) ? get_str.substr(0, pos) : get_str;
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

    if (num <= 0)
    {
        cout << "Missing size.";
        return 0;
    }
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
        s[idx](arr, num);                        // thực hiện sort
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