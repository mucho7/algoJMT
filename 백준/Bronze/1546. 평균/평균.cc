#include <iostream>

int main() {

  int a, n, sum=0, max=0;
  
  scanf("%d", &n);
  if(n>1000) return 0;
  
  for(int i=0; i<n; i++){
    scanf("%d", &a);
    
    if(max<a) max = a;
    sum += a;
  }
  double avg = double(sum)*100/n/max;
  printf("%f", avg);
  return 0;
}