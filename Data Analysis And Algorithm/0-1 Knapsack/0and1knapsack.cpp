#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct objects
{
    int id;
    int weight;
    int profit;
};

int knapsack(objects obj[], int size, int cap)
{
    vector<vector<int>> dp(size + 1, vector<int>(cap + 1, 0));

    for (int i = 1; i <= size; ++i)
    {
        for (int w = 1; w <= cap; ++w)
        {
            if (obj[i - 1].weight <= w)
            {
                dp[i][w] = max(obj[i - 1].profit + dp[i - 1][w - obj[i - 1].weight], dp[i - 1][w]);
            }
            else
            {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[size][cap];
}

int main()
{
    int size, capacity;
    cout << "Enter Size & capacity: ";
    cin >> size >> capacity;
    objects obj[size];
    for (int i = 0; i < size; i++)
    {
        cout << "Enter " << i + 1 << " Weight and Profit: ";
        obj[i].id = i + 1;
        cin >> obj[i].weight >> obj[i].profit;
    }
    cout << "Maximum Profit: " << knapsack(obj, size, capacity) << endl;
    return 0;
}