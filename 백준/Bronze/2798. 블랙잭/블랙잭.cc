#include <iostream>
using namespace std;

int main() {
  int n, m, sum=0, ans=0;
  int arr[100]={};

  cin >> n >> m;
  
  if(n<3 || n>100) return 0;
  if(m<10 || m>3000000) return 0;
  
  for(int i=0; i<n; i++){
    cin >> arr[i];
    if(arr[i]<0 || arr[i]>1000000) return 0;
  }

  for(int i=0; i<n-2; i++){
    for(int j=i+1; j<n-1; j++){
      for(int k=j+1; k<n; k++){
        sum = arr[i]+arr[j]+arr[k];
        if(sum>ans && sum<=m) ans = sum;
      }
      
    }
  }
  
  cout << ans; 
  
  return 0;
}