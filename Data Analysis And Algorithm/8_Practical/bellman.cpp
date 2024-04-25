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
    graph.BellmanFord();
    cout << endl;
    return 1;
}