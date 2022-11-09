#include <iostream>

int main() {

  int a, b, n, i=0;

  scanf("%d", &n);

  while(i<n)
  {
    scanf("%d", &a);
    scanf("%d", &b);
    printf("%d\n", a+b);
    i++;
  }

  return 0;
}