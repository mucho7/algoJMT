function solution(n, wires) {
    // 완탐이 아닌 방법이 없나...
    let answer = n;
    const graph = Array.from({ length: n + 1 }, () => Array(n + 1).fill(false));

    wires.forEach(([wireA, wireB]) => {
        graph[wireA][wireB] = true;
        graph[wireB][wireA] = true;
    })
    
    wires.forEach(([wireA, wireB]) => {
        let cursor = 0;
        const visited = Array(n + 1).fill(false);
        graph[wireA][wireB] = false;
        graph[wireB][wireA] = false;
        
        const queue = [wireA];
        while (queue.length > 0) {
            if (wireA === 3 && wireB === 4) console.log(queue)
            const node = queue.pop();
            visited[node] = true;
            cursor += 1;
            graph[node].forEach((line, index) => {
                if (line && !visited[index]) {
                    queue.push(index);
                }
            })
        }
        if (wireA === 3 && wireB === 4) console.log(n - cursor)
        
        graph[wireA][wireB] = true;
        graph[wireB][wireA] = true;
        answer = Math.min(answer, Math.abs(n - cursor * 2));
    })
    
    return answer;
}