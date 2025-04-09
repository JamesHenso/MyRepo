#pragma once
using namespace std;

int maxBit(int *a, int n, long long &counting)
{
    int res = 0;
    for (int i = 0; i < n; ++i)
    {
        counting += 2;
        int bit = 0;
        int tmp = a[i];
        while (tmp)
        {
            counting++;
            ++bit;
            tmp /= 2;
        }
        if (bit > res)
            res = bit;
    }
    counting += 2;
    return res;
}

void radixSort(int *a, int L, int R, int bit, long long &counting)
{
    if (bit == -1)
    {
        counting++;
        return;
    }
    if (L >= R)
    {
        counting++;
        return;
    }
    int i = L, j = R;
    while (true)
    {
        counting++;
        while ((a[i] >> bit & 1) == 0 && i <= j)
        {
            counting += 2;
            i++;
        }
        while ((a[j] >> bit & 1) == 1 && i <= j)
        {
            counting += 2;
            j--;
        }
        if (i > j)
        {
            counting++;
            break;
        }
        swap(a[i], a[j]);
    }
    counting += 5;

    // mang hien tai la a[L...j,i,...R]
    // phan hoach 2 mang va goi de quy ham radixSort
    radixSort(a, L, j, bit - 1, counting);
    radixSort(a, i, R, bit - 1, counting);
}

void radixSort(int *a, int n, long long &counting)
{
    int bit = maxBit(a, n, counting);
    radixSort(a, 0, n - 1, bit, counting);
}