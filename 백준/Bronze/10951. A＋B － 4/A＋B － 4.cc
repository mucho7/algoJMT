#include <iostream>

int main() {

  int a, b, n, x, i=0, j;
  

  
  while(scanf("%d %d", &a, &b)!=EOF){
    if(a<0 || b>10) return 0;
    printf("%d\n", a+b);

  }

  return 0;
}