from collections import Counter

def solution(str1, str2):
    def make_multiset(s):
        multiset = []
        for i in range(len(s) - 1):
            pair = s[i:i+2].lower()
            if pair.isalpha():
                multiset.append(pair)
            elif pair[0].isalpha() and pair[1].isalpha():
                multiset.append(pair)
        return multiset

    lst1 = make_multiset(str1)
    lst2 = make_multiset(str2)

    counter1 = Counter(lst1)
    counter2 = Counter(lst2)

    intersection = sum((counter1 & counter2).values())
    
    union = sum((counter1 | counter2).values())

    if union == 0:
        return 65536
    return int((intersection / union) * 65536)
