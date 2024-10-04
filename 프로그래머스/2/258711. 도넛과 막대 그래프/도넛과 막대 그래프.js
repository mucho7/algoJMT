

function solution(edges) {
    // answer : [정점, 도넛, 막대모양, 8자]
    // 정점 : only out
    // 도넛 : n개의 정점 + n개의 간선 || one way, circular
    // 막대 : n개의 정점 + n - 1개의 간선 || 
    // 8자 : 2n + 1개의 정점 + 2n + 2개의 간선 || two way, circular
    
    // 정점을 찾고 정점에서 나가는 간선의 수가 집단(?)의 수와 동일
    // 정점에서 1다리 건넌 node를 기준으로 탐색
    const answer = [0, 0, 0, 0];
    const length = edges.length + 1
    
    const graph = {};
    const inDegree = Array(length).fill(0);
    const outDegree = Array(length).fill(0);
    
    // 주어진 간선을 순회하며 
    // 정점 탐색 => 시작은 없지만 끝만 존재하는 점을 찾아야함
    // 그래프 기록 => 나중에 순회하면서 뭔지 알아야함 
    edges.forEach(([start, end]) => {
        if (!graph[start]) {
            graph[start] = [];
        }
        if (!graph[end]) {
            graph[end] = [];
        }

        graph[start].push(end);
        
        outDegree[start]++;
        inDegree[end]++;
    });
    const visited = Array(length).fill(false);
    
    // 정점에서 시작하여 연결된 그래프의 종류를 파악해야함
    const findGraph = (start) => {
        const stack = [start];
        let ans = 0

        while (stack.length > 0) {
            const node = stack.pop();
            if (!visited[node]) {
                visited[node] = true; // 노드 방문 처리

                // 인접 노드들을 스택에 추가
                for (const subNode of graph[node]) {
                    stack.push(subNode);
                }
                ans = Math.max(ans, graph[node].length)
            } 
            
            if (stack.includes(start)){
                return [1, ans]
            }
        }

        return [1, 0];
    };
    
    // 정점 찾기 (out-degree는 있지만 in-degree는 없는 노드)
    for (let i = 1; i < length; i++) {
        if (outDegree[i] >= 2 && inDegree[i] === 0) {
            answer[0] = i; // 정점 발견
            
            // 정점에서 연결된 그래프 탐색
            for (const start of graph[i]) {
                const [nodes, edges] = findGraph(start);
                // 도넛, 막대, 8자 탐색
                if (nodes === edges) {
                    answer[1]++; // 도넛 모양
                } else if (nodes === edges + 1) {
                    answer[2]++; // 막대 모양
                } else if (nodes === edges - 1) {
                    answer[3]++; // 8자 모양
                } 
            }
        }
    }
    
    return answer;
}