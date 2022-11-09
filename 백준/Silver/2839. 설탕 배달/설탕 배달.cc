#include <iostream>

int main() {
  int n, ans, i, m;
  scanf("%d", &n);
  if(n<3 || n>5000) return 0;
  m = n/5;
  for(i=m; i>=0; i--){
    m = n - 5*i;
    if((m%3) == 0) {
      ans = i+(m/3);
      break;
    }
    ans = -1;
  }
  
  printf("%d", ans);
  
  return 0;
  
}