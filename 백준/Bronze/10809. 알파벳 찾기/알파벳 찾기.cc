#include <iostream>
 //a=97

int main() {
  int n, x;
  char ar[100]={};
  scanf("%s", ar);

  
    for(int j=0; j<26; j++){
      for(int i=0; i<100; i++){
      if(j+97 == int(ar[i])){n=i; break;}
      else n=-1;
      }
      printf("%d ", n);
    }

    return 0;
}