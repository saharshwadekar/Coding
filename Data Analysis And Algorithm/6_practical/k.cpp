#include <bits/stdc++.h>

using namespace std;

struct Edge{
    int src, dest, wt;
};

void weightsort(Edge edges[], int E)
{
    for(int i = 1; i <= E-1; i++)
    {
        int j = i;
        Edge key = edges[i];
        while(--j>=0 && edges[j].wt > key.wt)
            edges[j+1] = edges[j];
        edges[j+1] = key;
    }
}

int findUparent(int parent[],int i)
{
    if(i == parent[i]) return i;
    return findUparent(parent, parent[i]);
}

void krushkal(Edge edges[], int E, int V)
{
    weightsort(edges,E);

    int* parent = new int[V];
    for(int i = 0 ;i < V; ++i)
        parent[i] = i;

    int weight = 0;

    cout << endl<< endl;
    for(int i = 0 ;i < E && V-1; i++)
    {
        int sp = findUparent(parent, edges[i].src); 
        int dp = findUparent(parent, edges[i].dest);
        if(sp != dp){
            parent[edges[i].dest] = sp;
            cout << edges[i].src << " " << edges[i].dest << " " << edges[i].wt << endl;
            weight += edges[i].wt;
            V--;
        }
    }

    cout << "Total Cost : " << weight << endl;

    delete[] parent;
}

int main()
{
    int V, E;
    cin >> V >> E;
    Edge* edges = new Edge[E];
    for(int i = 0 ;i < E; ++i)
    {
        cin >> edges[i].src >> edges[i].dest >> edges[i].wt ; 
    }
    krushkal(edges,E,V);
    delete[] edges;
    return 0;
}


/**
 * 
 *

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