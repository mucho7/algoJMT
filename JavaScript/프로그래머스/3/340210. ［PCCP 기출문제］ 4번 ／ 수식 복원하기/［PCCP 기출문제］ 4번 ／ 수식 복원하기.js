const plusString = (a, b, n = 10) => {
    return parseInt(a, n) + parseInt(b, n)
}

const minusString = (a, b, n = 10) => {
    return parseInt(a, n) - parseInt(b, n)
}

const checkIsSysAvailable = (left, right, systemArr, operator) => {
    const ansSet = new Set();
    for (const systemNum of systemArr) {
        const temp = operator(left, right, systemNum).toString(systemNum);
        ansSet.add(temp);
    }
    if (ansSet.size === 1) return ansSet.values().next().value
    else return false
}

const getAnswer = (formula, systemArr) => {
    let corAns = '?';

    let [left, operator, right, _] = formula

    switch (operator) {
        case '+':
            const plusRes = checkIsSysAvailable(left, right, systemArr, plusString);
            if (plusRes) corAns = plusRes
            break;
        case '-':
            const minusRes = checkIsSysAvailable(left, right, systemArr, minusString);
            if (minusRes) corAns = minusRes
            break;
    }
    return corAns
}

function solution(expressions) {
    // 진법 특징상 n - 1의 천장이 있음
    // 해당 천장을 파악하는 형식으로 가야할듯
    // 덧셈은 천장의 최소치를 확인시켜줌
    // 뺄셈의 경우 바닥(0)을 뚫을 경우 천장을 파악 가능
    
    // 천장을 모를 때
    // 천장 이상의 10진법 결과를 값으로 가지면 ?
    const answer = [];
    const formulas = [];
    
    let ceiling = 2;
    for (const expression of expressions) {
        // 8을 쓰면 9진법임! 확실함!
        const temporaryArr = [...expression
                              .split('')
                              .filter(part => !isNaN(part)) 
                              .map(Number)
                             ];
        const maxNum = Math.max(...temporaryArr.map((num) => parseInt(num)))
        if (maxNum >= ceiling) {
            ceiling = maxNum + 1;
        }
    }
    
    let systemArr = Array.from({ length: 10 - ceiling }, (_, i) => ceiling + i);
    
    
    for (const expression of expressions) {
        // 좌항과 우항은 두자릿수 이하의 정수
        // 좌항 >= 우항
        let [left, operator, right, _, result] = expression.split(' ');

        
        if (result === 'X') {
            // 나중에 풀게 보관
            formulas.push([left, operator, right, _])
            continue;
        }; 
        
        switch (operator) {
            case '+': 
                systemArr = systemArr.filter((sys) => plusString(left, right, sys) === parseInt(result, sys));
                break;
            case '-':
                systemArr = systemArr.filter((sys) => minusString(left, right, sys) === parseInt(result, sys));
                break;
            default:
                throw new Error('으아닛 고등수학이다')
        }
        console.log(systemArr)
    }
    
    for (const formula of formulas) {
        const corAns = getAnswer(formula, systemArr);
        formula.push(corAns);
        
        answer.push(formula.join(' '));
    }
    
    return answer;
}