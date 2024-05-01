#include <iostream>
#include <stack>
#include <queue>

using namespace std;

void DFS(int V, int E) {
    int A[V][V] = {0};
    int f;

    for(int i = 0; i < E; ++i) {
        int x, y;
        cin >> x >> y;
        A[x][y] = 1;
        A[y][x] = 1;
    }

    stack<int> s;
    int visited[V] = {0};

    cout << "Starting vertex: ";
    cin >> f;

    s.push(f);
    while(!s.empty()) {
        int i = s.top();
        s.pop();
        if(visited[i] == 1) continue;
        visited[i] = 1;
        cout << i << "->";
        for(int j = 0; j < V; j++) {
            if(A[i][j] == 1 && visited[j] == 0)
                s.push(j);
        }
    }
}

int main() {
    int V, E;
    cout << "Enter number of vertices and edges: ";
    cin >> V >> E;
    DFS(V, E);
    return 0;
}
