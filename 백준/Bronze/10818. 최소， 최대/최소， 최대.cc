#include <iostream>

int main() {

  int n, x, i, j, min=1000000, max=-10000000;
  
  scanf("%d", &n);
  if(n<1 || n>1000000) return 0;
  
  for(i=0; i<n; i++){
    scanf("%d", &x);
    if(max<x) max=x;
    if(min>x) min=x;
  }

  printf("%d %d", min, max);
  return 0;
}