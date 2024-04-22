#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
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
        Edge reverseEdge = {dest, src, weight};
        edges.push_back(reverseEdge);
    }

    void primMST()
    {
        vector<int> key(V, INT_MAX);
        vector<bool> mstSet(V, false);
        vector<int> parent(V, -1);

        key[0] = 0;

        for (int count = 0; count < V - 1; count++)
        {
            int u = minKey(key, mstSet);
            mstSet[u] = true;

            for (const Edge &edge : edges)
            {
                if (!mstSet[edge.dest] && edge.src == u && edge.weight < key[edge.dest])
                {
                    parent[edge.dest] = u;
                    key[edge.dest] = edge.weight;
                }
            }
        }

        cout << "\nPrim's MST:" << endl;
        for (int i = 1; i < V; i++)
            cout << parent[i] << " - " << i << " : " << key[i] << endl;
    }

    int minKey(vector<int> &key, vector<bool> &mstSet)
    {
        int minIndex, min = INT_MAX;
        for (int v = 0; v < V; v++)
        {
            if (!mstSet[v] && key[v] < min)
            {
                min = key[v];
                minIndex = v;
            }
        }
        return minIndex;
    }
};

int main()
{
    int V, E;
    cout << "Enter the number of vertices and edges: ";
    cin >> V >> E;

    Graph graph(V);
    cout << "Enter source, destination, and weight for each edge:" << endl;
    for (int i = 0; i < E; i++)
    {
        int src, dest, weight;
        cin >> src >> dest >> weight;
        graph.addEdge(src, dest, weight);
    }

    graph.primMST();

    return 0;
}