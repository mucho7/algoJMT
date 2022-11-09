#include <iostream>

int main() {

  int a, b, n, i, j;

  scanf("%d", &n);

  if(n>100 || n<0) return 0;
  for(j=0; j<n; j++){
    for(i=j; i>=0; i--){
      printf("*");
    }
    printf("\n");
  }

  return 0;
}