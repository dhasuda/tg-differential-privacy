#include<iostream>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;

struct node {
    string value
    node * left;
    node * right;
}

typedef struct node node;

void readFile()
{
    ifstream file;
    file.open ("treeText.txt");
    if (!file.is_open()) return;
    int i = 0;
    string word;
    while (file >> word && i < 100) {
        cout << word << '\n';
        i++;
    }
}

int main() {
    readFile();
    return 0;
}