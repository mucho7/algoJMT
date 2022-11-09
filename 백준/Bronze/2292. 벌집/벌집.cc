#include <iostream>

int main() {
    int n, ans, honey=1;
  
  scanf("%d", &n);
  n -= 1;
  
  while(n>0){
    n -= 6*honey;
    honey++;
  }
  printf("%d", honey);
  
}