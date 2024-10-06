function solution(friends, gifts) {
    let answer = 0;
    const giftLevelObj = {}
    
    for (const friend of friends) {
        giftLevelObj[friend] = { sum : 0 };
        for (const friend2 of friends) {
            if (friend === friend2) continue;
            giftLevelObj[friend][friend2] = 0
        }        
    }
    
    
    for (const gift of gifts) {
        const [giver, taker] = gift.split(" ");
        giftLevelObj[giver][taker] += 1;
        giftLevelObj[taker][giver] -= 1;
        
        giftLevelObj[taker].sum -= 1;
        giftLevelObj[giver].sum += 1;
    }
    
    for (const friend of friends) {
        let cnt = 0
        for (const friend2 of friends) {
            if (friend === friend2) continue;
            
            if (giftLevelObj[friend][friend2] > 0) cnt++;
            else if (giftLevelObj[friend][friend2] === 0) {
                if (giftLevelObj[friend].sum > giftLevelObj[friend2].sum) cnt ++;
            }
        }        
        answer = Math.max(cnt, answer)
    }
    
    return answer;
}