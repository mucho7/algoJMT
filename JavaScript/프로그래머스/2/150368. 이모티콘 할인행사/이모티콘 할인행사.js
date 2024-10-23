function solution(users, emoticons) {
    // 할인율은 10%, 20%, 30%, 40%
    const discountRates = [10, 20, 30, 40]
    // 브루탈
    // 각 이모티콘 별로 할인했을 시 가격이 들어있는 array를 만들고
    // 이모티콘 할인율이 얼마인지 정하는 array또한 만듬
    // 7^4 개의 경우의 수가 있고 이를 모두 확인해보자
    
    // 이를 통해 최종적으로 subscibe가 가장 높고, sales가 높을 때의 값을 찾는다
    let subscibe = 0;
    let sales = 0;
    
    const calculateCombinations = (index, emoticonPriceInfo) => {
        if (index === emoticons.length) {
            let curSubs = 0;
            let curSales = 0;
            for (const user of users) {
                const [wantRate, ceiling] = user;
                let sum = 0;
                for (const info of emoticonPriceInfo) {
                    const [price, dcRate] = info;
                    if (dcRate >= wantRate) sum += price
                }
                if (sum >= ceiling) curSubs += 1;
                else curSales += sum;
            }
            if (curSubs > subscibe) {
                subscibe = curSubs;
                sales = curSales;
            } else if (curSubs === subscibe) sales = Math.max(sales, curSales)
            return;
        }

        // 현재 이모티콘의 모든 할인된 가격에 대해 재귀 호출
        for (const discount of discountRates) {
            const discountedPrice = emoticons[index] * (100 - discount) / 100
            emoticonPriceInfo.push([discountedPrice, discount]);
            calculateCombinations(index + 1, emoticonPriceInfo);
            emoticonPriceInfo.pop();
        }
    }
    
    calculateCombinations(0, [])
    
    return [subscibe, sales];
}