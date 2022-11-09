#include <iostream>

int main() {
    int A, B, C, ans;
  
  scanf("%d %d %d", &A, &B, &C);
  
  if(C-B<0) printf("-1");
  else if((C-B)==0) printf("-1");
  else {
    ans = A/(C-B);
    printf("%d", ans+1);
  }
}