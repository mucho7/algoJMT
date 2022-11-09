#include <iostream>
using namespace std;
long long pado[101] = {0,1,1,1, };



int main() {
  
  for(int i=4; i<101; i++){
    pado[i] = pado[i-2] + pado[i-3];
  }
  
  int a, b;
  cin >> b;

  for(int i=0; i<b; i++){
    cin >> a;
    cout << pado[a] << endl;
  }
  
}

/*if(n<3){
    return pado[n];
  }
  else{
    pado[n] = pad(n-2) + pad(n-3);
    return pado[n];
    */