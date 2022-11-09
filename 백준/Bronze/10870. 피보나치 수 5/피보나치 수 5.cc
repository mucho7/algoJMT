#include <iostream>

int pivo(int a){
  if(a <= 1) return a;
  else{
    return pivo(a-2) + pivo(a-1);
  }
    
}
  

int main() {
  int n;
  scanf("%d", &n);
  if(n<0 || n>20) return 0;
  
  printf("%d", pivo(n));
  
  return 0;
}