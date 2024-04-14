#include <iostream>
#include <vector>
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
        Edge reverseEdge = {dest, src, weight}; 
        edges.push_back(reverseEdge);
    }

    int findParent(int parent[], int i)
    {
        if (parent[i] == i)
            return i;
        return findParent(parent, parent[i]);
    }

    void unionSets(int parent[], int rank[], int x, int y)
    {
        int xRoot = findParent(parent, x);
        int yRoot = findParent(parent, y);

        if (rank[xRoot] < rank[yRoot])
            parent[xRoot] = yRoot;
        else if (rank[xRoot] > rank[yRoot])
            parent[yRoot] = xRoot;
        else
        {
            parent[yRoot] = xRoot;
            rank[xRoot]++;
        }
    }

    void kruskalMST()
    {
        sort(edges.begin(), edges.end(), [](Edge a, Edge b)
             { return a.weight < b.weight; });

        vector<Edge> result;
        int parent[V], rank[V];
        for (int i = 0; i < V; i++)
        {
            parent[i] = i;
            rank[i] = 0;
        }

        int e = 0, i = 0;
        while (e < V - 1 && i < edges.size())
        {
            Edge nextEdge = edges[i++];
            int x = findParent(parent, nextEdge.src);
            int y = findParent(parent, nextEdge.dest);

            if (x != y)
            {
                result.push_back(nextEdge);
                unionSets(parent, rank, x, y);
                e++;
            }
        }

        cout << "Kruskal's MST:" << endl;
        for (Edge edge : result)
            cout << edge.src << " - " << edge.dest << " : " << edge.weight << endl;
    }

    void primMST()
    {
        vector<int> key(V, INT32_MAX);
        vector<bool> mstSet(V, false);
        vector<int> parent(V, -1);

        key[0] = 0; 

        for (int count = 0; count < V - 1; count++)
        {
            int u = minKey(key, mstSet);
            mstSet[u] = true;

            // Update key values and parent for adjacent vertices of the picked vertex
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
        int minIndex, min = INT32_MAX;
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

    graph.kruskalMST();
    graph.primMST();

    return 0;
}