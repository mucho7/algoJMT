#include <iostream>

int main() {

  int n, x, i, j, min, max=0;
  
  int a[9];
  
  for(i=0; i<9; i++){
    scanf("%d", &a[i]);
    if(max<a[i]){ x=i+1; max=a[i];}
  }
  
  printf("%d %d", max, x);
  
  return 0;
}