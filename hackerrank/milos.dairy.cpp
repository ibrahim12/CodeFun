#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    
    int n;
    int p;
    vector<int> a;
    
    string out = "YES";
    
    cin >> n;
    while(cin >> p){
        a.push_back(p);
    }
    

    if(a.size() == 1)
        out = "YES";
            
    
    for(int i =0; i < a.size(); i++){
        cout << a[i] << endl;
    }
    
    
    return 0;
}
