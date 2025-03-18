import re
from collections import Counter

def solution(s):
    s = re.findall(r'\d+', s)
    counter = Counter(s)
    
    answer = [int(num) for num, _ in counter.most_common()]
    
    return answer
