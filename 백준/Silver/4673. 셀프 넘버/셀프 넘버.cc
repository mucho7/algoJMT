#include <iostream>

int self_num(int a){
  int sum=a;
  while(a != 0){
    sum += a%10;
    a = a/10;
  }
  return sum;
}


int main() {
  int a;
  int total[10001]={};
  
  for(int i=1; i<10001; i++){
    a = self_num(i);
    if(a<10001) total[a]=1;
  }
  for(int i=1; i<10001; i++){
    if(total[i] == 0) printf("%d\n", i);
  }
  return 0;
}