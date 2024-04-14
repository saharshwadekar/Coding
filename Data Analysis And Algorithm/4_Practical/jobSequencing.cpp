#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool profitSort(vector<int> first, vector<int> second)
{
    return first[2] > second[2];
}

int main()
{
    int max_deadline = 0;
    int job_size = 0;
    int max_profit = 0;

    cout << "Enter No. of jobs: ";
    cin >> job_size;

    vector<vector<int> > job_table(job_size);
    vector<bool> time_slot(job_size, false);

    for (int i = 0; i < job_size; i++)
    {
        int temp_deadline = 0, temp_profit = 0;
        cout << "Enter Job " << i + 1 << " deadline and profit: ";
        cin >> temp_deadline >> temp_profit;
        max_deadline = max(max_deadline, temp_deadline);
        job_table[i].push_back(i+1);
        job_table[i].push_back(temp_deadline);
        job_table[i].push_back(temp_profit);
        // job_table[i] = {i + 1, temp_deadline, temp_profit}; // Job ID, Deadline, Profit
    }

    sort(job_table.begin(), job_table.end(), profitSort);

    vector<int> job_id(max_deadline + 1, -1); // Initialize job_id with -1

    for (int i = 0; i < job_size; i++)
    {
        int deadline = job_table[i][1];
        while (deadline > 0)
        {
            if (!time_slot[deadline])
            {
                time_slot[deadline] = true;
                job_id[deadline] = job_table[i][0]; // Assign job ID to the deadline slot
                max_profit += job_table[i][2];      // Add profit of the assigned job
                break;
            }
            deadline--;
        }
    }

    cout << "Job sequence to maximize profit: ";
    for (int i = 1; i <= max_deadline; i++)
    {
        if (job_id[i] != -1)
        {
            cout << "J" << job_id[i] << "->";
        }
    }
    cout << endl
         << "Total Profit: " << max_profit;

    return 0;
}
