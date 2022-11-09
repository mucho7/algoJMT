#include <iostream>

int main() {
  int n, sum=0;
  scanf("%d", &n);
  char ar[n];
  scanf("%s", ar);
  
  for(int i=0; i<n; i++){
    sum += ar[i] - '0';
  }
  
  printf("%d", sum);
  
    return 0;
}