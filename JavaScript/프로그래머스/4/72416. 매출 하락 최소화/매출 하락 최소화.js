function solution(sales, links) {
    const n = sales.length;
    const tree = Array.from({ length: n }, () => []);
    const dp = Array.from({ length: n }, () => [0, 0]);

    // 트리 생성
    links.forEach(([parent, child]) => {
        tree[parent - 1].push(child - 1);
    });

    // DP 정의: dfs로 트리 탐색
    function dfs(node) {
        dp[node][0] = 0; // node가 참석하지 않을 때 최소 비용
        dp[node][1] = sales[node]; // node가 참석할 때 최소 비용

        if (tree[node].length === 0) return;

        let extraCost = Infinity;
        tree[node].forEach((child) => {
            dfs(child);
            // node가 참석하지 않으면, 자식 중 최소 하나는 참석해야 한다.
            dp[node][0] += Math.min(dp[child][0], dp[child][1]);
            // node가 참석하는 경우, 자식이 참석할 필요가 없다.
            dp[node][1] += Math.min(dp[child][0], dp[child][1]);
            // node가 참석하지 않는 경우, 자식 중 하나를 참석시키는 추가 비용 계산
            extraCost = Math.min(extraCost, dp[child][1] - Math.min(dp[child][0], dp[child][1]));
        });

        // 만약 node가 참석하지 않고, 모든 자식이 참석하지 않는 경우를 고려하여 extraCost를 추가
        dp[node][0] += extraCost;
    }

    // 루트 노드부터 시작 (0번 노드)
    dfs(0);

    // 루트 노드가 참석할 때와 참석하지 않을 때 중 최소값 반환
    return Math.min(dp[0][0], dp[0][1]);
}
