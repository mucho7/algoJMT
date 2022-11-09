#include <iostream>

int main() {

  int a, n, m=1, sum = 0;
  int score[1000]={0};
  
  scanf("%d", &n);

  for(int i=0; i<n; i++){
    scanf("%d", &m);
    if(m>1000 || m<1) return 0;
    for(int j=0; j<m; j++){
      scanf("%d", &score[j]);
      sum += score[j];
    }
    int avg = (sum)/m;
    int count=0;
    for(int j=0; j<m; j++){
      if(avg<score[j]) count++;
    }
    printf("%.3f%%\n", double(count)/m*100);
    sum=0;
  }
  return 0;
}