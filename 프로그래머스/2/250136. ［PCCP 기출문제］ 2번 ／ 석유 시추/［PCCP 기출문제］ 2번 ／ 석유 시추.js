function solution(land) {
    let answer = 0;
    const landDepth = land.length;
    const landLength = land[0].length;
    
    const visited = Array(landDepth).fill().map(() => Array(landLength).fill(false));

    let oilId = 0;
    const oilLand = Array(landDepth).fill().map(() => Array(landLength).fill(-1));
    const oilMap = new Map();

    const findOilLand = (x, y) => {
        const queue = [[x, y]];
        let res = 0;

        while (queue.length > 0) {
            const [curX, curY] = queue.shift();

            if (
                curX >= 0 && curX < landLength &&
                curY >= 0 && curY < landDepth &&
                land[curY][curX] === 1 && !visited[curY][curX]
            ) {
                res += 1;
                visited[curY][curX] = true;
                oilLand[curY][curX] = oilId;

                const reachList = [[0, 1], [0, -1], [1, 0], [-1, 0]];
                for (const [dx, dy] of reachList) {
                    queue.push([curX + dx, curY + dy]);
                }
            }
        }

        return res;
    };

    
    for (let i = 0; i < landLength; i++) {
        for (let j = 0; j < landDepth; j++) {
            if (!visited[j][i] && land[j][i] === 1) {
                const oilCnt = findOilLand(i, j);
                oilMap.set(oilId, oilCnt);
                oilId += 1;
            }
        }
    }
    
    for (let i = 0; i < landLength; i++) {
        let tmp = [];
        let sum = 0;
            for (let j = 0; j < landDepth; j++) {
                if (oilLand[j][i] >= 0 && !tmp.includes(oilLand[j][i])) {
                    const id = oilLand[j][i]; 
                    tmp.push(id);
                    sum += oilMap.get(id);
            }
        }
        // 뽑을 수 있는 석유량이 가장 많은 경우를 answer에 저장
        if (answer < sum) answer = sum;
    }
    
    return answer;
}