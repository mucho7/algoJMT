#include <iostream>

int main() {

  int a, b, n, i, j;

  scanf("%d", &n);
  if(n>100 || n<0) return 0;
  
  for(j=0; j<n; j++){
    for(i=n; i>j+1; i--){
      printf(" ");
    }
    for(i=0; i<=j; i++){
      printf("*");
    }
    printf("\n");
  }

  return 0;
}