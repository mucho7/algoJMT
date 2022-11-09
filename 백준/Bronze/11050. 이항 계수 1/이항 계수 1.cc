#include <iostream>
using namespace std;

int pac(int a){
  int ans=1;
  for(int i=1; i<=a; i++){
    ans = ans*i;
  }
  return ans;
}

int main() {
  int a, b;
  cin >> a >> b;
  
  cout << pac(a)/pac(b)/pac(a-b);
  
  return 0;
}