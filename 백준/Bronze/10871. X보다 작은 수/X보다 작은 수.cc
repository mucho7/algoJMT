#include <iostream>

int main() {

  int a, b, n, x, i=0, j;

  scanf("%d", &n);
  scanf("%d", &x);
  
  if(n<=1 || x>=10000) return 0;
  
  while(i<n){
    scanf("%d", &a);
    if(a<x) printf("%d\n", a);
    i++;
  }

  return 0;
}