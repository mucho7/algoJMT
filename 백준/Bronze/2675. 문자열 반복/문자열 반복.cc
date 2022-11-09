#include <iostream>
#include <string.h>

int main() {
  int test, x;
  char ar[20]={};
  scanf("%d", &test);
  if(test<1 || test>1000) return 0;
  
  for(int j=0; j<test; j++){
    scanf("%d", &x);
    if(x<0 || x>8) break;
    scanf("%s", ar);
    if((int)strlen(ar)<1 || (int)strlen(ar)>20) break;
    for(int k=0; k<(int)strlen(ar); k++){
      for(int i=0; i<x; i++){
      printf("%c", ar[k]);
      }
    }
    printf("\n");
  }
  
    return 0;
}
