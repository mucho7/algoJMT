function findLastNonZeroIndex(arr, startIndex) {
  for (let i = startIndex - 1; i >= 0; i--) {
    if (arr[i] !== 0) {
      return i + 1;
    }
  }
  return 0; // 모든 값이 0!
}

function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    
    // 물륭창고에서 처음 차에서 실어서 출발할 물류량
    // 수거할 수 있거나 배달할 수 있는 가장 먼곳까지 이동하자
    let goal = Math.max(findLastNonZeroIndex(deliveries, n),
                        findLastNonZeroIndex(pickups, n));
    
    while (goal !== 0) {
        let deliCnt = cap;
        let pickCnt = 0;
        
        while (deliveries.length) {
            let target = deliveries.pop();
            const deliverAmount = Math.min(target, deliCnt)
            target -= deliverAmount;
            deliCnt -= deliverAmount;
            
            if (target > 0) {
                deliveries.push(target)
                break;
            }
        }
        
        while (pickups.length) {
            let target = pickups.pop();
            const pickupAmount = Math.min(target, cap - pickCnt)
            target -= pickupAmount;
            pickCnt += pickupAmount;
            
            if (target > 0) {
                pickups.push(target)
                break;
            }
        }
        
        // 물류창고 도착 시, 이동거리  * 2
        answer += 2 * goal;
        goal = Math.max(deliveries.length ,pickups.length);
    };
    
    return answer;
}