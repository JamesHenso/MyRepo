#pragma once
using namespace std;

void shellSort(int *a, int n, int &counting)
{
    int i, j, tmp;
    for (int gap = n / 2; gap > 0; gap /= 2)
    {
        counting++;
        for (i = gap; i < n; i += 1)
        {
            counting++;
            tmp = a[i];
            for (j = i; j >= gap && a[j - gap] > tmp; j -= gap)
            {
                counting++;
                a[j] = a[j - gap];
            }
            a[j] = tmp;
        }
    }
    counting++;
}
