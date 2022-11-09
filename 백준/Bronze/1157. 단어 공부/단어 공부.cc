#include <iostream>
#include <string.h>

int main() {
  int a[26]={}, max=0, ch=0;
  char word[1000000]={}, x;
  scanf("%s", word);
  int size =(int)strlen(word);
  
  for(int i=0; i<size; i++){
    if(word[i]>96) word[i] -= 32;
    for(int j=0; j<27; j++){
      if(int(word[i])==j+65) a[j]++;
    }
  }
  
  for(int j=0; j<27; j++){
    if(a[j] > max) {
      max = a[j];
      x=j;
      }
  }
  for(int j=0; j<27; j++){
    if(max==a[j]) ch++;
  }
  
  if(ch>1) printf("?");
  else printf("%c", int(x)+65);


  return 0;
}
