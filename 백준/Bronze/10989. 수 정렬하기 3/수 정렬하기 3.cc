#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  int n;
  cin >> n;
  
  int arr[10001]={};

  for(int i=0; i<n; i++){
    int in;
    cin >> in;
    arr[in]+=1;
    
    if(in<0) return 0;
  } 

  for(int i=1; i<10001; i++){
    for(int j=0l;j<arr[i]; j++){
      cout << i << "\n";
    }
  }

  return 0;
}