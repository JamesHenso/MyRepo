#pragma once
using namespace std;

void bubbleSort(int *a, int n, long long & counting)
{
    for (int i = 0; i < n - 1; ++i)
    {
        counting++;
        for (int j = n - 1; j > i; --j)
        {
            counting += 2;
            if (a[j] < a[j - 1])
                swap(a[j], a[j - 1]);
        }
    }
    counting += 2;
}
