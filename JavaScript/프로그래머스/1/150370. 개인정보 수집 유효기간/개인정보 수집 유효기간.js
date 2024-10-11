const getDateNum = (dateStr) => {
    // console.log(dateStr)
    const dates = dateStr.split(".").map((date) => parseInt(date))
    const todayNum = (dates[0] - 2020) * 28 * 12 + dates[1] * 28 + dates[2];
    
    return todayNum;
}

function solution(today, terms, privacies) {
    const answer = [];
    
    const todayNum = getDateNum(today)
    
    const expireTerms = {};
    terms.forEach((term) => {
        const [expireType, expireMonths] = term.split(" ");
        expireTerms[expireType] = expireMonths * 28;
    });
    
    privacies.forEach((privacy, index) => {
        const [collectDay, expireType] = privacy.split(" ");
        const expireDateNum = getDateNum(collectDay) + expireTerms[expireType];
        
        if (expireDateNum <= todayNum) answer.push(index + 1);
    })
    
    return answer;
}