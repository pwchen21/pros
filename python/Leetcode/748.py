from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        candidate=[]
        for x in licensePlate:
            if x > "9":
                candidate.append(x.lower())
        
        freq=Counter(candidate)
        print(freq)
        words.sort(key=lambda x:len(x))
        #print(words)
        #print('plate:', freq)

        for w in words:
            print(w)
            if len(w) < len(candidate):
                continue
            word_freq= Counter(w)
            print(word_freq)
            for c, count in freq.items():
                print('word_freq', word_freq)
                print(' c, count', c, count) # plate item and number
                if (c not in word_freq) or (word_freq[c] < count):
                    print('here')
                    break
            else:
                print(w)
                return w
            
A=Solution()
A.shortestCompletingWord("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"])