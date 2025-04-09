#pragma once
using namespace std;
#include <ctime>

void quickSort(int *a, int low, int high, long long &counting)
{
    int i = low;
    int j = high;
    int pivot = a[(i + j) / 2];
    int tmp;

    while (i <= j)
    {
        counting += 2;
        while (a[i] < pivot)
        {
            i++;
            counting++;
        }
        while (a[j] > pivot)
        {
            counting++;
            j--;
        }
        if (i <= j)
        {
            tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
            i++;
            j--;
        }
    }
    counting += 3;
    if (j > low)
    {
        counting++;
        quickSort(a, low, j, counting);
    }
    if (i < high)
    {
        counting++;
        quickSort(a, i, high, counting);
    }
}

void quickSort(int *a, int n, long long &counting)
{
    quickSort(a, 0, n - 1, counting);
}