#pragma once
using namespace std;

void heapify(int *a, int i, int n, long long &counting)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[largest] < a[left])
    {
        counting++;
        largest = left;
    }

    if (right < n && a[largest] < a[right])
    {
        counting++;
        largest = right;
    }

    if (largest != i)
    {
        counting++;
        swap(a[largest], a[i]);
        heapify(a, largest, n, counting);
    }
}

void heapSort(int *a, int n, long long &counting)
{
    for (int i = n / 2 - 1; i >= 0; --i)
    {
        counting++;
        heapify(a, i, n, counting);
    }
    for (int i = n - 1; i >= 0; --i)
    {
        counting++;
        swap(a[0], a[i]);
        heapify(a, 0, i, counting);
    }
    counting += 2;
}
