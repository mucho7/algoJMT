
function solution(triangle) {
    const triLength = triangle.length;
    const tempTri = triangle.map(layer => [...layer]);

    for (let i = 0; i < triLength - 1; i++) {

        // n층엔 수가 n개 있음
        for (let j = 0; j < i + 1; j++) {
            // 내려올려는 윗층 세입자
            const parentNum = tempTri[i][j];
            tempTri[i + 1][j] = Math.max(tempTri[i + 1][j], triangle[i + 1][j] + parentNum)
            tempTri[i + 1][j + 1] = Math.max(tempTri[i + 1][j + 1], triangle[i + 1][j + 1] + parentNum)
        }
    }
    
    const answer = Math.max(...tempTri[triLength - 1])
    
    return answer;
}