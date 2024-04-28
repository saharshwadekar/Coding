#include <iostream>
#include <climits>

using namespace std;

void prims(int E, int V)
{
    int A[V][V];
    int *MST = new int[V];
    int *parent = new int[V];
    int *key = new int[V];
    int iter = V;

    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
            A[i][j] = INT_MAX;

        key[i] = INT_MAX;
        MST[i] = 0;
        parent[i] = -1;
    }

    for (int i = 0; i < E; ++i)
    {
        int x, y, wt;
        cin >> x >> y >> wt;
        A[x][y] = wt;
        A[y][x] = wt;
    }

    key[0] = 0;
    parent[0] = 0;

    while (iter)
    {
        int minIndex = 0;
        for (int i = 1; i < V; ++i)
        {
            if (key[i] < key[minIndex] && !MST[i])
                minIndex = i;
        }

        MST[minIndex] = 1;

        for (int i = 0; i < V; ++i)
        {
            if (key[i] > A[minIndex][i] && !MST[i])
            {
                parent[i] = minIndex;
                key[i] = A[minIndex][i];
            }
        }
        iter--;
    }

    cout << endl
         << endl;
    for (int i = 1; i < V; ++i)
    {
        if (parent[i] != -1)
            cout << parent[i] << " - " << i << " : " << A[i][parent[i]] << endl;
    }

    delete[] MST;
    delete[] parent;
    delete[] key;
}

int main()
{
    int V, E;
    cin >> V >> E;
    prims(E, V);
    return 0;
}

/*
7 9
4 6 6
0 3 1
0 4 4
2 3 2
4 5 3
2 5 4
1 2 5
0 1 2
5 6 2
*/

/*
7 9
4 6 6
0 3 1
0 4 4
2 3 2
4 5 3
2 5 4
1 2 5
0 1 2
5 6 2
*/