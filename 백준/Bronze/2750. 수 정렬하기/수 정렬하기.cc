#include <iostream>
using namespace std;



int main() {
  int n, temp;
  int arr[1000];
  int ans[1000];

  cin >> n;
  if(n<1 || n>1000) return 0;

  for(int i=0; i<n; i++){
    cin >> arr[i];
  }

  for(int i=0; i<n-1; i++){
    for(int j=i+1; j<n; j++){
      if(arr[i]>arr[j]) {
        temp=arr[j];
        arr[j]=arr[i];
        arr[i]=temp;
      }
    }
  }

  
  for(int i=0; i<n; i++){
    cout << arr[i] << endl;
  }
  
  return 0;
}