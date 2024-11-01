

function solution(n, s, a, b, fares) {
    // s : start 둘 모두의 시작지점
    // a : a의 goal
    // b : b의 goal
    
    // 그래프 저장
    const graph = Array.from({length: n + 1}, () => Array(n + 1).fill(Infinity));
    for (const [to, from, fare] of fares) {
        graph[to][from] = fare;
        graph[from][to] = fare;
    }
    
    for (let i = 1; i <= n; i++) {
        graph[i][i] = 0;
    }
    
    for (let k = 1; k <= n; k++) {
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                if (i === j) continue;
                if (graph[i][k] === Infinity || graph[k][j] === Infinity) continue;
                
                graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j])
            }
        }
    }
    
    let answer = Infinity;
    for (let i = 1; i <= n; i++) {
        // i = 중간지점
        // graph[s][i] : 시작점에서 중간지점까지의 거리
        // graph[i][x] : 중간지점에서 각 종점까지의 거리
        answer = Math.min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    }
    
    return answer;
}