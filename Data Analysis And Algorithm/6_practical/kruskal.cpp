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

    return 0;
}

/* 10 16
0 1 4
0 3 1
1 3 4
3 7 5
7 9 2
3 9 6
1 9 10
1 2 4
9 6 4
9 8 3
4 6 2
4 2 2
6 8 3
6 5 3
2 5 1
8 5 5
*/