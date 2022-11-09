#include <iostream>

int main() {

  int a, b, n, i=0;

  scanf("%d", &n);
  a=n;

  if(n>1000000) return 0;
  
  while(i<n)
  {
    printf("%d\n", a);
    i++; a--;
  }

  return 0;
}