#include <iostream>

int main() {

  int a, b, c, x, y, i, N[10]={0};
  scanf("%d %d %d", &a, &b, &c);
  if(a<100 || a>1000) return 0;
  if(b<100 || b>1000) return 0;
  if(c<100 || c>1000) return 0;  

  x = a*b*c;
  
  while(x!=0){
    N[x%10] += 1;
    x=x/10;
  }

  for(i=0; i<10; i++){
    printf("%d\n", N[i]);
  }
  return 0;
}