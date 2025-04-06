#pragma once
using namespace std;

void mergeArray(int *a, int *a1, int n1, int *a2, int n2, int &counting)
{
    int pos = 0, pos1 = 0, pos2 = 0;
    while (pos1 < n1 && pos2 < n2)
    {
        counting += 3;
        if (a1[pos1] < a2[pos2])
            a[pos++] = a1[pos1++];
        else
            a[pos++] = a2[pos2++];
    }
    while (pos1 < n1)
    {
        a[pos++] = a1[pos1++];
        counting++;
    }
    while (pos2 < n2)
    {
        a[pos++] = a2[pos2++];
        counting++;
    }
    counting += 4;
}

void mergeSort(int *a, int idxL, int idxR, int &counting)
{
    int n = idxR - idxL + 1;
    if (n <= 1)
    {
        counting++;
        return;
    }
    int half = n / 2;

    // create 2 sub arrays
    int *a1 = new int[half];
    int *a2 = new int[n - half];
    for (int i = 0; i < half; ++i)
    {
        counting++;
        a1[i] = a[idxL + i];
    }
    for (int i = 0; i < n - half; ++i)
    {
        counting++;
        a2[i] = a[idxL + half + i];
    }
    counting += 2;
    // sort each subarray then merge them into a
    mergeSort(a1, 0, half - 1, counting);
    mergeSort(a2, 0, n - half - 1, counting);
    mergeArray(a, a1, half, a2, n - half, counting);

    delete[] a1;
    delete[] a2;
}

void mergeSort(int *a, int n, int &counting)
{
    mergeSort(a, 0, n - 1, counting);
}