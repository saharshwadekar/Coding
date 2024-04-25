#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

struct Edge
{
    int src, dest;
};

class Graph
{
    int V;
    vector<Edge> edges;

public:
    Graph(int vertices) : V(vertices) {}

    void addEdge(int src, int dest)
    {
        Edge edge = {src, dest};
        edges.push_back(edge);
    }

    void BFS(int start)
    {
        map<int, bool> visited;
        queue<int> container;
        container.push(start);
        visited[start] = true;

        while (!container.empty())
        {
            int u = container.front();
            container.pop();
            cout << u << " ";

            for (const auto &edge : edges)
            {
                if (edge.src == u && !visited[edge.dest])
                {
                    container.push(edge.dest);
                    visited[edge.dest] = true;
                }
            }
        }
    }
};

int main()
{
    int V, E;
    cout << "Enter Number of Vertices and Edges in Graph : ";
    cin >> V >> E;
    Graph graph(V);

    cout << "Edge  : src dest" << endl;
    for (int i = 1; i <= E; ++i)
    {
        int s, d;
        cin >> s >> d;
        graph.addEdge(s, d);
    }

    int startVertex;
    cout << "Enter the starting vertex for BFS: ";
    cin >> startVertex;

    cout << "BFS traversal starting from vertex " << startVertex << ": ";
    graph.BFS(startVertex);
    cout << endl;

    return 0;
}

//output

PS D:\Coding\Data Analysis And Algorithm\10_practical> cd "d:\Coding\Data Analysis And Algorithm\10_practical\" ; if ($?) { g++ BFS.cpp -o BFS } ; if ($?) { .\BFS }
Enter Number of Vertices and Edges in Graph : 4 7
Edge  : src dest
1 2
1 4
2 1
2 3
3 1
3 4
4 1
Enter the starting vertex for BFS: 1
BFS traversal starting from vertex 1: 1 2 4 3