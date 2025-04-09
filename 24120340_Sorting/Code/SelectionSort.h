#pragma once
using namespace std;

void selectionSort(int *a, int n, long long &counting)
{
    int i, j, posMin;
    for (i = 0; i < n - 1; i++)
    {
        counting++;
        posMin = i;
        for (j = i + 1; j < n; j++)
        {
            counting += 2;
            if (a[j] < a[posMin])
                posMin = j;
        }
        swap(a[posMin], a[i]);
    }
    counting += 2;
}
