#include <iostream>

int main() {
  int n=0, m, ans=0;
  scanf("%d", &n);
  if(n<1 || n>100) return 0;
  int ar[n];
  
  for(int i = 0; i<n; i++){
    scanf("%d", &ar[i]);
    if(ar[i]<1 || ar[i]>1000) return 0;
    else if(ar[i] == 1) ar[i] = 0;
    
    for(int j = 2; j<ar[i]; j++){
      if(ar[i]%j == 0) ar[i]=0;
    }
    if(ar[i] != 0) ans++;
  }
  
  printf("%d", ans);
  
  return 0;
  
}