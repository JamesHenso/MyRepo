#pragma once

void countingSort(int *a, int n, int &counting)
{
    int maxValue = a[0];
    for (int i = 1; i < n; i++)
    {
        counting++;
        maxValue = max(maxValue, a[i]);
    }

    int *count = new int[maxValue + 1]{};
    int *output = new int[n];

    for (int i = 0; i < maxValue + 1; i++)
    {
        counting++;
        count[i] = 0;
    }
    for (int i = 0; i < n; i++)
    {
        counting++;
        count[a[i]]++;
    }
    for (int i = 1; i < maxValue + 1; i++)
    {
        counting++;
        count[i] += count[i - 1];
    }
    for (int i = n - 1; i >= 0; i--)
    {
        counting++;
        output[count[a[i]] - 1] = a[i];
        count[a[i]]--;
    }
    for (int i = 0; i < n; i++)
    {
        counting++;
        a[i] = output[i];
    }

    counting += 6;

    delete[] count;
    delete[] output;
}