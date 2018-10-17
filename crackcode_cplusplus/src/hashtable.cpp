/*
 * C++ Program For Hash Tables
 Properties:
 1. Search is O(1)
 2. Insert is O(1) / Delete is O(1)
 3. However, worst case scenarior require going through entire hash, so O(n)

 Requires hash table to be properly spread without colliision; this requires a very good hash function. 

 
 */

// include statements
#include<iostream>
#include<cstdlib>
#include<string>
#include<cstudio>

using namespace std;
const int TABLE_SIZE = 128; // this is the hardcoded table size of each hash table

/*
* Hashtable Class
*/
class HashElement {
	public:
		int key;
		int value;
		HashElement(int key, int value) {
			this->key = key;
			this->value = value;
		}
};

/*
Has the functions to:
1. insert
2. search
3. remove
4. construct/delete
*/
class HashTable {
	private:
		HashElement **table; // declare pointer to the pointer of the table
	public:
		// constructor for hashtable and initialize all elements to NULL
		HashTable() { 
			table = new HashElement * [TABLE_SIZE];
			for (int i=0; i<TABLE_SIZE; i++) {
				table[i] = NULL;
			}
		}


		int Hash(int key) {
			return key % TABLE_SIZE;
		}

		void Insert(int key, int value) {
			int hash = Hash(key); // use the hash function modulo to get a hash

			// move down the line until empty table element & key is not reached
			while (table[hash] != NULL && table[hash]->key != key) {
				hash = Hash(hash+1);
			}

			if (table[hash]!= NULL)
				delete table[hash];

			table[hash] = new HashElement(key, value)
		}

		int Search(int key) {
			int hash = Hash(key);

			// move down the line until empty table element & unique key
			while (table[hash] != NULL && table[hash]->key != key) {
				hash = Hash(hash+1);
			}
			if (table[hash] == NULL)
				return -1
			else
				return table[hash]->value;
		}

		void Delete(int key) {
			int hash = Hash(key);
			while (table[hash] != NULL)
		    {
		        if (table[hash]->key == key)
		            break;
		        hash = Hash(hash + 1);
		    }
            if (table[hash] == NULL)
		    {
                cout<<"No Element found at key "<<key<<endl;
                return;
            }
            else
            {
                delete table[hash];
            }
            cout<<"Element Deleted"<<endl;
		}
        ~HashMap()
		{
            for (int i = 0; i < TABLE_SIZE; i++)
            {
                if (table[i] != NULL)
                    delete table[i];
                delete[] table;
            }
        }
};

/*
Testing function grabbed from online
*/

/*
 * Main Contains Menu
 */
int main()
{
    HashMap hash;
    int key, value;
    int choice;
    while (1)
    {
        cout<<"\n----------------------"<<endl;
        cout<<"Operations on Hash Table"<<endl;
        cout<<"\n----------------------"<<endl;
        cout<<"1.Insert element into the table"<<endl;
        cout<<"2.Search element from the key"<<endl;
        cout<<"3.Delete element at a key"<<endl;
        cout<<"4.Exit"<<endl;
        cout<<"Enter your choice: ";
        cin>>choice;
        switch(choice)
        {
        case 1:
            cout<<"Enter element to be inserted: ";
            cin>>value;
            cout<<"Enter key at which element to be inserted: ";
            cin>>key;
            hash.Insert(key, value);
            break;
        case 2:
            cout<<"Enter key of the element to be searched: ";
            cin>>key;
            if (hash.Search(key) == -1)
            {
	        cout<<"No element found at key "<<key<<endl;
	        continue;
	    }
	    else
	    {
	        cout<<"Element at key "<<key<<" : ";
	        cout<<hash.Search(key)<<endl;
	    }
            break;
        case 3:
            cout<<"Enter key of the element to be deleted: ";
            cin>>key;
            hash.Remove(key);
            break;
        case 4:
            exit(1);
        default:
           cout<<"\nEnter correct option\n";
       }
    }
    return 0;
}


