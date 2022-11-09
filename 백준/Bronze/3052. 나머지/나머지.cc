#include <iostream>

int main() {

  int a, i, same, diff=0, j, N[10]={0};
  
  for(i=0; i<10; i++){
    scanf("%d", &a);
    if(a<0 || a>1000) return 0;
    N[i]=a%42;
  }

  for(i=0; i<10; i++){
    same=0;
    for(j=i+1; j<10; j++){
      if(N[i]==N[j]) same++;
    }
    if(same==0) diff++;
  }
  printf("%d", diff);
  
  return 0;
}