#include <iostream>
#include <cstdlib>
using namespace std;

#define MAX 20 // max size of the adjacency matrix


class AdjacencyMatrix {
	private:
		int n; // size
		int **adj;
		bool *visited;

	public:
		AdjacencyMatrix(int n) {
			this->n = n;
			visited = new bool [n];

			// initialize all elements to 0
			adj = new int* [n];
			for (int i=0; i<n; i++) {
				adj[i] = new int [n];
				for (int j=0; j<n; j++) {
					adj[i][j] = 0;
				}
			}
		}

		void add_edge(int origin, int dest) {
			if (origin < n || dest > n || origin < 0 || dest < 0) {
				cout<<"Invalid edge!"<<endl;
			}
			else {
				adj[origin-1][dest-1] = 1;
			}
		}
        void display()
        {
            int i,j;
            for(i = 0;i < n;i++)
            {
                for(j = 0; j < n; j++)
                    cout<<adj[i][j]<<"  ";
                cout<<endl;
            }
        }
}

int main()
{
    int nodes, max_edges, origin, destin;
    cout<<"Enter number of nodes: ";
    cin>>nodes;
    AdjacencyMatrix am(nodes);
    max_edges = nodes * (nodes - 1);
    for (int i = 0; i < max_edges; i++)
    {
        cout<<"Enter edge (-1 -1 to exit): ";
        cin>>origin>>destin;
        if((origin == -1) && (destin == -1))
            break;
        am.add_edge(origin, destin);
    }
    am.display();
    return 0;
}