#include <iostream>
using namespace std;

int main() {
  int a, b;
  int gcd, bigger, small;
  cin >> a >> b;

  if(a<1 || b<1) return 0;
  if(a>10000 || b>10000) return 0;
  
  if(a>b){
    bigger = a;
    small = b;
    }
  else {
    bigger = b;
    small = a;
  }

  
  for(int i=bigger; i>0; i--){
    if(a%i==0 && b%i==0) {
      gcd = i;
      break;
    }
  }
  
  
  cout << gcd << "\n";
  cout << a*b/gcd << "\n";
  
  return 0;
}