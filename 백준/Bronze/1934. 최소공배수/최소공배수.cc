#include <iostream>
using namespace std;

int main() {
  int a, b, t, c;
  int gcd=1, big, small;
  cin >> t;
  
  for(int i=0; i<t; i++){
    cin >> a >> b;
    if(a>b){
      big = a; small =b;
    }
    else{
      big = b; small = a;
    }

    while(small>0){
      if(big%small==0){
        gcd = small;
        break;
      }
      else{
        c = big;
        big = small;
        small = c-c/small*small;
      }
    }
    
    cout << a*b/gcd << "\n";
  }
  return 0;
}