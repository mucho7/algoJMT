#include <iostream>

int main() {

  int a, b, c, n, x, i=0, j;
  
  scanf("%d", &n);
  if(n<0 || n>100) return 0;
  x=n;
  do{
    a = x/10;
    b = x%10;
    c = (a+b)%10;
    x= 10*b + c;
    i++;
  }while(x!=n);
    
  printf("%d\n", i);
  return 0;
}