#include <iostream>
#include <algorithm>
using namespace std;
struct objects
{
    int id;
    double weight;
    double profit;
    double ratio;
};
bool sortWeightAcc(objects a, objects b) { return a.weight < b.weight; }
bool sortProfitDec(objects a, objects b) { return a.profit > b.profit; }
bool sortRatioDec(objects a, objects b) { return a.ratio > b.ratio; }
double knapsack(objects obj[], int size, int cap)
{
    int capacity = cap;
    double profit = 0;
    for (int i = 0; i < size && capacity > 0; i++)
    {
        if (obj[i].weight <= capacity)
        {
            capacity -= obj[i].weight;
            profit += obj[i].profit;
        }
        else
        {
            double new_weight = (capacity / obj[i].weight) * obj[i].weight;
            double new_profit = (capacity / obj[i].weight) * obj[i].profit;

            capacity -= new_weight;
            profit += new_profit;
        }
    }

    return profit;
}
double maximumProfit(objects obj[], int size, int cap)
{
    sort(obj, obj + size, sortProfitDec);
    return knapsack(obj, size, cap);
}
double minimumWeight(objects obj[], int size, int cap)
{
    sort(obj, obj + size, sortWeightAcc);
    return knapsack(obj, size, cap);
}
double maximumRatio(objects obj[], int size, int cap)
{
    sort(obj, obj + size, sortRatioDec);
    return knapsack(obj, size, cap);
}
int main()
{
    int size, capacity;
    cout << "Enter Size & capacity :";
    cin >> size >> capacity;
    objects obj[size];
    for (int i = 0; i < size; i++)
    {
        cout << "Enter " << i + 1 << " Weight and Profit : ";
        obj[i].id = i + 1;
        cin >> obj[i].weight >> obj[i].profit;
        obj[i].ratio = (obj[i].profit / obj[i].weight);
    }
    cout << "Maximum Profit : " << maximumProfit(obj, size, capacity) << endl;
    cout << "Minimum Weight : " << minimumWeight(obj, size, capacity) << endl;
    cout << "Maximum Ratio(profit/weight) : " << maximumRatio(obj, size, capacity) << endl;
    return 0;
}