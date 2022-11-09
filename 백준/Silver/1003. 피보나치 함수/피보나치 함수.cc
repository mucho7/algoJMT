#include <iostream>
using namespace std;

int main() {
  int n, a;
  int fibo[41] = {0, 1, 1};

  for(int i=3; i<41; i++){
    fibo[i]=fibo[i-1] + fibo[i-2];
  }
  
  cin >> n;

  for(int i=0; i<n; i++){
    cin >> a;
    if(a==1){
      cout << "0 1" << endl;
    }
    else if(a==0){
      cout << "1 0" << endl;
    }
    else cout <<fibo[a-1]<<" "<<fibo[a]<<endl;//피보나치 출력
  }
}