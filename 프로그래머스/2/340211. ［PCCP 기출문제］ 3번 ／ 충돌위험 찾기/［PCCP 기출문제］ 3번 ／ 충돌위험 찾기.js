const rangeLikePython = (start, end, filler, axis) => {
    let res = [];
    
    const step = start < end ? 1 : -1;
    
    if (axis === 'x') {
        for (let i = start + step; i !== end + step; i += step) {
            res.push(`${i},${filler}`);
        }
    } else {
        for (let i = start + step; i !== end + step; i += step) {
            res.push(`${filler},${i}`);
        }
    }
    return res;
}

function solution(points, routes) {
    // 로봇은 반드시 최단경로로 움직이고 x축 이동을 우선시 한다
    // 이때 충돌위험이 총 몇번 발생하는가?
    // 충돌위험이란 1칸 안에 2대 이상의 로봇이 모이는 것
    
    /* 
        로봇이 이동해야하는 경로에 대해서는 이미 알고 있음
        로봇이 어느 시간에 어디에 있는지 정보를 획득할 수 있음
        장애물도 없는데 일단 시간에 따른 로봇의 위치를 만든 다음 비교해도 될듯?
    */
    const getRobotMove = (robotRoute) => {
        let [robotX, robotY] = points[robotRoute[0] - 1]
        const res = [`${robotX},${robotY}`]
        
        for (let i = 1; i < robotRoute.length; i++ ) {
            const goal = points[robotRoute[i] - 1]
            if (robotX !== goal[0]){
                res.push(...rangeLikePython(robotX, goal[0], robotY, 'x'));
                robotX = goal[0];    
            }
            if (robotY !== goal[1]){
                res.push(...rangeLikePython(robotY, goal[1], goal[0], 'y'));
                robotY = goal[1];
            }
        }
        return res
    }
    
    let answer = 0;
    const moveArr = [];
    let maxLen = 0;
    
    for (const robotRoute of routes) {
        const res = getRobotMove(robotRoute);
        moveArr.push(res);
        maxLen = Math.max(res.length, maxLen);
    }
    
    for (let i = 0; i < maxLen; i++) {
        const seen = new Set();
        const sameSet = new Set();
        
        for (let j = 0; j < routes.length; j++) {
            if (moveArr[j].length <= i) continue;
            
            if (seen.has(moveArr[j][i])) sameSet.add(moveArr[j][i])
            else seen.add(moveArr[j][i]);
        }
        answer += sameSet.size;
    }
    
    return answer;
}