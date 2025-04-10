#pragma once
using namespace std;

void heapify(int *a, int i, int n)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[largest] < a[left])
    {
        largest = left;
    }

    if (right < n && a[largest] < a[right])
    {
        largest = right;
    }

    if (largest != i)
    {
        swap(a[largest], a[i]);
        heapify(a, largest, n);
    }
}

void heapSort(int *a, int n)
{
    for (int i = n / 2 - 1; i >= 0; --i)
    {
        heapify(a, i, n);
    }
    for (int i = n - 1; i >= 0; --i)
    {
        swap(a[0], a[i]);
        heapify(a, 0, i);
    }
}
