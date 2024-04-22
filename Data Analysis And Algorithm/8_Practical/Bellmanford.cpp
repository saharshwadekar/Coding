#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

struct Edge
{
    int src, dest, weight;
};

class Graph
{
    int V;
    vector<Edge> edges;

public:
    Graph(int vertices) : V(vertices) {}

    void addEdge(int src, int dest, int weight)
    {
        Edge edge = {src, dest, weight};
        edges.push_back(edge);
    }

    void BellmanFord()
    {
        sort(edges.begin(), edges.end(), [](Edge a, Edge b)
             { return a.src < b.src; });
        vector<pair<int, int>> load(V + 1, make_pair(INT_MAX, -1));
        load[1].first = 0;
        bool changes = true;
        for (int i = 0; i < (V - 1) && changes; ++i)
        {
            changes = false;
            for (auto &e : edges)
            {
                if (load[e.src].first + e.weight < load[e.dest].first)
                {
                    changes = true;
                    load[e.dest].first = load[e.src].first + e.weight;
                    load[e.dest].second = e.src;
                }
            }
        }

        for (int i = 1; i <= V; ++i)
            cout << i << " : " << load[i].first << " " << load[i].second << endl;

        int last = V;
        vector<int> path;
        while (last != -1)
        {
            path.push_back(last);
            last = load[last].second;
        }
        for (auto i : path)
            cout << i << " <- ";
    }

    void printmatrix(vector<vector<int>>& Matrix){
            for (int x = 1; x <= V; ++x)
            {
                for (int y = 1; y <= V; ++y)
                {
                    if (x == y)
                    {
                        cout << "0\t";
                        Matrix[x][y] = 0;
                    }
                    else if (Matrix[x][y] == INT_MAX)
                        cout << "Inf\t";
                    else
                        cout << Matrix[x][y] << "\t";
                }
                cout << endl;
            }
            cout << endl
                << endl;
        }

    void FloydWarshall()
    {
        vector<vector<int>> Matrix(V + 1, vector<int>(V + 1, INT_MAX));
        for (auto &e : edges)
        {
            Matrix[e.src][e.dest] = e.weight;
        }
        printmatrix(Matrix);
        for (int i = 1; i <= V; ++i)
        {
            for (int x = 1; x <= V; ++x)
            {
                for (int y = 1; y <= V && x != i; ++y)
                {
                    int second = Matrix[x][i] + Matrix[i][y];
                    if (second < 0) second *= -1;
                    if (y != i && (Matrix[x][y] > second ))
                        Matrix[x][y] = Matrix[x][i] + Matrix[i][y];
                }
            }
            cout << endl << "Iteration : " << i  << endl;
            printmatrix(Matrix);
        }
    }
};

int main()
{
    int V, E;
    cout << "Enter Number of Vertices and Edges in Graph : ";
    cin >> V >> E;
    Graph graph(V);

    cout << "Edge  : src dest weight" << endl;
    for (int i = 1; i <= E; ++i)
    {
        int s, d, w;
        // cout << "Edge " << i << " : ";
        cin >> s >> d >> w;
        graph.addEdge(s, d, w);
    }

    // graph.BellmanFord();
    // graph.FloydWarshall();

    cout << endl;
    return 1;
}

/// V E  7 10
/*
1 2 6
1 3 5
1 4 5
2 5 -1
3 5 1
3 2 -2
4 3 -2
4 6 -1
5 7 3
6 7 3


4 7

1 2 3
1 4 7
2 1 8
2 3 2
3 1 5
3 4 1
4 1 2

   */