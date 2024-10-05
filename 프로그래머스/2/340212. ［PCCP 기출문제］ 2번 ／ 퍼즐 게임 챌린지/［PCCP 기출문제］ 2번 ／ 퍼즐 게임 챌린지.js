const solveProblems = (diffs, times, level) => {
    let spentTime = 0;
    
    for (let i = 0; i < diffs.length; i++) {
        if (diffs[i] > level) { // 첫번째 문제는 무조건 1이라 맞춤!
            spentTime += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i];
        }
        else spentTime += times[i];
    }
    
    return spentTime;
}

function solution(diffs, times, limit) {
    // 이분탐색 백트랙킹
    let right = 100000;
    let left = 0;
    let result = right;
    
    while (left <= right) {
        const level = Math.floor((left + right) / 2);
        const res = solveProblems(diffs, times, level);
        
        if (res <= limit) {
            result = level;
            right = level - 1;  // 범위를 줄여가며 탐색
        } else {
            left = level + 1;
        }
    }
    
    return result;
}