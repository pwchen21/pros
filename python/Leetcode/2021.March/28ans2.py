import collections
class Solution:
    def originalDigits(self, s):
        counter = collections.Counter(s)
        print('0:', counter)
        res = []
        # print(counter)
        distinguish = {"z": "0", "w": "2", "u": "4", "f":"5", "x":"6", "v":"7", "g":"8", "i":"9", "o":"1", "t":"3"}
        word = {"0": "zero", "1": "one", "2": "two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
        for k,v in distinguish.items():
            print('k, v:', k, v)
            repeat = counter[k]
            print('repeat:', repeat)
            wordCounter = collections.Counter(word[v])
            print('wc:', wordCounter)
            for k in wordCounter.keys():
                print('k:', k)
                wordCounter[k] *= repeat
            for _ in range(repeat):
                res.append(v)
            counter -= wordCounter
        print("".join(sorted(res)))
            
A=Solution()
A.originalDigits("owoztneoer")
#96

