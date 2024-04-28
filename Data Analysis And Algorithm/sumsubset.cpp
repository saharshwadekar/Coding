#include <bits/stdc++.h>

using namespace std;

class Solution
{
    vector<int> setofint;
    int summ;
    vector<string> results;

public:
    Solution(vector<int> si, int s) : setofint(si), summ(s) {}

    void sumSubsetProblem(int i, int value, string ans)
    {
        if (i == setofint.size())
        {
            if (value == summ)
            {
                results.push_back(ans);
            }
            return;
        }
        sumSubsetProblem(i + 1, value + setofint[i], ans + "1");
        sumSubsetProblem(i + 1, value              , ans + "0");
    }

    void printresult()
    {
        for (auto &ele : results)
        {
            cout << ele << "  ";
        }
    }
};

int main()
{
    // vector<int> a = {438, 702, 165, 831, 274, 509, 721, 88, 396, 625, 472, 209, 743, 55, 333, 678, 987, 112, 440, 856, 203, 578, 721};
    vector<int> a = {1, 2, 3, 4, 5, 6, 7};
    int sum = 11;
    Solution obj(a, sum);
    obj.sumSubsetProblem(0, 0, "");
    obj.printresult();
    return 0;
}
