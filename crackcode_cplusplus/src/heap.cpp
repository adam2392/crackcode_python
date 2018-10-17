/*
 * C++ Program to Implement Heap
 */
#include <iostream>
#include <cstdlib>
#include <vector>
#include <iterator>
using namespace std;

// Class declaration for a heap
class Heap 
{
	private:
		vector <int> heap;
		int left(int parent);
		int right(int parent);
		int parent(int child);
		void heapup(int index);
		void heapdown(int index);

	public:
		Heap() {}

		void Insert(int element);
		void DeleteMin();
		int GetMin();
		void DisplayHeap();
		int GetSize();
};

// Methods for the heap class
int Heap::GetSize()
{
	return heap.size(); // use vector's size function
}

void Heap::Insert(int element) {
	heap.push_back(element);
	heapup(heap.size() - 1);
}

void Heap::DeleteMin() {
	if (heap.size() == 0) {
		cout << "Heap is already empty!" << endl;
		return;
	}
	heap[0] = heap.at(heap.size() - 1); // point head to 2nd to last element
	heap.pop_back(); // pop off the last element
	heapdown(0);
	cout << "Element is deleted." << endl;
}

int Heap::GetMin() {
	if (heap.size() == 0) {
		return -1;
	} 
	else
		return heap.front(); // front of heap is the smallest
}

void Heap::DisplayHeap() {
	vector <int>::iterator pos = heap.begin();
	cout << "Heap --> ";
	while (pos != heap.end()) {
		cout<<*pos<<" "; //print out the value at pointer's address
		pos++; //increment iterator
	}
	cout<<endl;
}

// return's left child of a parent
int Heap::left(int parent) {
	int l = 2*parent+1;
	if (l < heap.size())
		return l;
	else
		return -1;
}

int Heap::right(int parent) {
	int r = 2*parent+2;
	if (r < heap.size())
		return r;
	else
		return -1;
}

int Heap::parent(int child) {
	int p = (child-1)/2;
	if (child == 0)
		return -1;
	else
		return p;
}

// Functions to maintain heap structure
void Heap::heapup(int in) {
	if (in >=0 && parent(in) >= 0 && heap[parent(in)] > heap[in]) {
		int temp = heap[in];
		heap[in] = heap[parent(in)];
		heap[parent(in)] = temp;
		heapup(parent(in));
	}
}

void Heap::heapdown(int in) {
	int child = left(in);
    int child1 = right(in);
    if (child >= 0 && child1 >= 0 && heap[child] > heap[child1])
    {
       child = child1;
    }
    if (child > 0)
    {
        int temp = heap[in];
        heap[in] = heap[child];
        heap[child] = temp;
        heapdown(child);
    }
}

/*
 * Main Contains Menu
 */
int main()
{
    Heap h;
    while (1)
    {
        cout<<"------------------"<<endl;
        cout<<"Operations on Heap"<<endl;
        cout<<"------------------"<<endl;
        cout<<"1.Insert Element"<<endl;
        cout<<"2.Delete Minimum Element"<<endl;
        cout<<"3.Extract Minimum Element"<<endl;
        cout<<"4.Print Heap"<<endl;
        cout<<"5.Exit"<<endl;
        int choice, element;
        cout<<"Enter your choice: ";
        cin>>choice;
        switch(choice)
        {
        case 1:
            cout<<"Enter the element to be inserted: ";
            cin>>element;
            h.Insert(element);
            break;
        case 2:
            h.DeleteMin();
            break;
        case 3:
            cout<<"Minimum Element: ";
            if (h.GetMin() == -1)
            {
                cout<<"Heap is Empty"<<endl;
            }
            else
                cout<<"Minimum Element:  "<<h.GetMin()<<endl;
            break;
        case 4:
            cout<<"Displaying elements of Hwap:  ";
            h.DisplayHeap();
            break;
        case 5:
            exit(1);
        default:
            cout<<"Enter Correct Choice"<<endl;
        }
    }
    return 0;
}