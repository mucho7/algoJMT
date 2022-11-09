#include <iostream>
#include <string.h>

int main() {
  int size, cnt;
  char word[100]={};
  scanf("%s", word);
  size = (int)strlen(word);
  cnt=size;
  
  for(int i=0; i<size; i++){
    if(word[i]=='=') {
      if(word[i-1]=='z'&&word[i-2]=='d') cnt -=2;
      else cnt--;
    }
    else if(word[i]=='-') cnt--;
    else if(word[i]=='j'){
      if(word[i-1]=='l'|| word[i-1]=='n') cnt--;
    }
  }
  printf("%d", cnt);
  
  return 0;
}
