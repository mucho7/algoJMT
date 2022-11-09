#include <iostream>
using namespace std;



int main() {
  int n, sum, ch;

  cin >> n;
  if(n<1 || n>1000000) return 0;

  for(int i=1; i<n; i++){
    sum = i;
    ch = i;
    
    while(ch!=0){
      sum+=ch%10;
      ch=ch/10; 
    }
    
    if(sum==n) {
      cout << i; 
      return 0;
    }
    
  }

  cout << "0";

  
  return 0;
}