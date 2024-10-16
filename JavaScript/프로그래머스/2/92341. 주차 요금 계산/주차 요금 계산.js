function solution(fees, records) {
    // 차량 번호가 작은 자동차부터!
    
    const [baseTime, baseFee, unitTime, unitFee] = fees;
    const midnightTime = 23 * 60 + 59;
    
    const carRecord = {};
    
    records.forEach((record) => {
        const [time, carNum, io] = record.split(" ");
        const numericTime = time.split(":")
                                .map((str) => parseInt(str))
                                .reduce((acc, cur, index) => acc + (index === 0 ? cur * 60 : cur), 0);
        if (!carRecord[carNum]) {
            carRecord[carNum] = [];
        }
        carRecord[carNum].push([numericTime, io])
    })
    
    const answer = Object.keys(carRecord).sort().map((carNum) => {
        let res = 0;
        let outFlag = false;
        carRecord[carNum].forEach(([numericTime, io]) => {
            switch(io) {
                case "IN":
                    res -= numericTime;
                    outFlag = false;
                    break;
                case "OUT":
                    res += numericTime;
                    outFlag = true;
                    break;
            }
        })
        if (!outFlag) res += midnightTime;
        res = baseFee + Math.ceil(Math.max(res - baseTime, 0) / unitTime) * unitFee
        
        return res
    })
    
    return answer;
}