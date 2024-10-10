function solution(h1, m1, s1, h2, m2, s2) {
    let answer = 0;
    
    const tik = () => {
        s1 += 1;
        
        if (s1 === 60) {
            s1 = 0;
            m1 += 1;
            
            if (m1 === 60) {
                m1 = 0;
                h1 += 1;
            }
        }
    }
    
    if (m1 === 0 && s1 === 0) answer += 1;

    while (h1 !== h2 || m1 !== m2 || s1 !== s2) {
        if ((h1 === 11 || h1 === 23) && m1 === 59 && s1 === 59) answer += 1;
        else {
            if (m1 === s1 && !(m1 === 0 && s1 === 0)) answer += 1;
            if ((h1 % 12) * 5 + Math.floor(m1 / 12) == s1 && !((h1 % 12 === 0) && m1 === 0 && s1 === 0)) answer += 1;    
        }
        tik();
    }
    
    return answer;
}