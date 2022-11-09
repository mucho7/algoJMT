#include <iostream>
#include <math.h>
int main() {
  int A, B, V;
  double ans;
  scanf("%d %d %d", &A, &B, &V);
  
  if(A-B<=0) return 0;
  else if(B<0 || A<0) return 0;
  else if(V-A<0) return 0;
  else {
    ans = ceil((double)(V-A)/(A-B));
    printf("%d", (int)ans+1);
  }
  return 0;
  
}