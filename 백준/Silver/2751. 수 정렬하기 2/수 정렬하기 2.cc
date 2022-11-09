#include <iostream>
#include <algorithm>
using namespace std;



int main() {
  int n;
  int arr[1000000];
  cin >> n;
  

  for(int i=0; i<n; i++){
    cin >> arr[i];
  } //스캔

  sort(arr, arr + n);

  
  for(int i=0; i<n; i++){
    cout << arr[i] << "\n";
  } //출력
  
  return 0;
}