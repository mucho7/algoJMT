#include <iostream>
int ans=1;

void pac(int a){
  if(a==0){
    printf("%d", ans);
  }
  else{
    ans = ans * a;
    a -= 1;
    pac(a);
  }
  
}


int main() {
  int n;
  scanf("%d", &n);
  if(n<0 || n>12) return 0;
  
  pac(n);
  return 0;
}