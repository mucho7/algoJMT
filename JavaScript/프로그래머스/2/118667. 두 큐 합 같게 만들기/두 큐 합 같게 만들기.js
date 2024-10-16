function solution(queue1, queue2) {
    let answer = 0;
    
    let firstSum = queue1.reduce((acc, cur) => acc+ cur, 0);
    let secondSum = queue2.reduce((acc, cur) => acc+ cur, 0);
    
    let firstCur = 0;
    let secondCur = queue1.length;
    
    const totalQueue = [...queue1, ...queue2]
    
    while (firstSum !== secondSum){ // 일단 예시를 위해 4로 고정
        if (firstSum < secondSum) {
            firstSum += totalQueue[secondCur];
            secondSum -= totalQueue[secondCur];
            secondCur += 1;
        } else {
            firstSum -= totalQueue[firstCur];
            secondSum += totalQueue[firstCur];
            firstCur += 1;
        }
        answer += 1;
        
        if (firstCur === secondCur || secondCur === totalQueue.length) {
            answer = -1;
            break;
        }
    }
    

    return answer;
}