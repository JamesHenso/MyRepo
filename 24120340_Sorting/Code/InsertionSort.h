#pragma once
using namespace std;

void insertionSort(int *a, int n, long long &counting)
{
    for (int i = 1; i < n; i++)
    {
        counting++;
        int cur = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > cur)
        {
            counting += 2;
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j + 1] = cur;
    }
    counting += 3;
}
