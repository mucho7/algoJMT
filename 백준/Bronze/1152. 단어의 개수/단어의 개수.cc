#include <iostream>
#include <string.h>

int main() {
  int num_word=1, size;
  char word[1000000]={};
  scanf("%[^\n]s", word);
  size = (int)strlen(word);
  if (size == 1){
    if( word[0] == ' '){
      printf("0\n");
      return 0;
    }
  }
  
  for(int i=1; i<size-1; i++){
    if(word[i]==32) num_word++;
  }
  printf("%d", num_word);
  
  return 0;
}
