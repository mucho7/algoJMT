#include <iostream>

int main() {
  int T, H, W, N, ans;
  scanf("%d", &T);

  for(int i=0; i<T; i++){
    scanf("%d %d %d", &H, &W, &N);
    if(N>H*W) return 0;
    else if(W>99 || W<1) return 0;
    else if(1>N)  return 0;
    else if(1>H)  return 0;
    else if(N%H==0){
      ans = 100*H+(N/H);
      printf("%d\n", ans);
    } 
    else{
    ans = 100*(N%H)+((N/H)+1);
    printf("%d\n", ans);
    }
  }
  
  return 0;
  
}