class TreeNode {
  constructor(node, x) {
    this.node = node; // 노드 번호
    this.x = x; // 노드의 x 좌표
    this.left = null; // 왼쪽 자식
    this.right = null; // 오른쪽 자식
  }
}

function insertNode(parent, child) {
    if (child.x < parent.x) {
        // 자식의 x 좌표가 부모보다 작으면 왼쪽에 추가
        if (!parent.left) {
            parent.left = child;
        } else {
            insertNode(parent.left, child);
        }
    } else {
        // 자식의 x 좌표가 부모보다 크면 오른쪽에 추가
        if (!parent.right) {
            parent.right = child;
        } else insertNode(parent.right, child);
    }
}

const preOrder = (node) => {
    if (!node) return [];
    const result = [];
    
    result.push(node.node);
    result.push(...preOrder(node.left))
    result.push(...preOrder(node.right))
    
    return result
}

const postOrder = (node) => {
    if (!node) return [];
    const result = [];
    
    result.push(...postOrder(node.left))
    result.push(...postOrder(node.right))
    result.push(node.node);
    
    return result
}

function solution(nodeinfo) {
    // 이진 트리
    // nodeinfo > index + 1의 번호를 가지는 노드의 [x, y]좌표
    const positionInfo = {}
    nodeinfo.forEach(([x, y], index) => {
        if (!positionInfo[y]) positionInfo[y] = []
       positionInfo[y].push({ node: index + 1, x: x});
    })  
    // 가장 y축이 높은 node = root
    const nodYList = Object.keys(positionInfo).reverse();
    const rootNodeY = nodYList[0];
    const rootNodeData = positionInfo[rootNodeY][0];
    const rootNode = new TreeNode(rootNodeData.node, rootNodeData.x);

    // y 축을 따라서 부모 자식을 정하고 Tree 구성
    for (const yAxix of nodYList) {
        if (yAxix === rootNodeY) continue;
        const yAxisInfo = positionInfo[yAxix];
         yAxisInfo.forEach(({node, x}) => {
            const newNode = new TreeNode(node, x);
            insertNode(rootNode, newNode)
        })
    }
    // 전위 순회 및 후위순회한 결과를 도출
    return [preOrder(rootNode), postOrder(rootNode)];
}   