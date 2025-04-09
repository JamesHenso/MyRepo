#pragma once
using namespace std;

void shakerSort(int *a, int n, long long &counting)
{
    bool swapped = true;
    int start = 0, end = n - 1;

    while (swapped)
    {
        counting++;
        swapped = false;
        for (int i = start; i < end; ++i)
        {
            counting += 2;
            if (a[i] > a[i + 1])
            {
                swap(a[i], a[i + 1]);
                swapped = true;
            }
        }
        counting++;
        if (!swapped)
            break;
        swapped = false;
        --end;
        for (int i = end - 1; i >= start; --i)
        {
            counting += 2;
            if (a[i] > a[i + 1])
            {
                swap(a[i], a[i + 1]);
                swapped = true;
            }
        }
        ++start;
    }
    counting += 3;
}