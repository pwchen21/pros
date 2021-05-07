class Solution:
    def spellchecker(self, wordlist, queries):
        words = {w: w for w in wordlist}
        cap = {w.lower(): w for w in wordlist[::-1]}
        vowel = {re.sub("[aeiou]", '#', w.lower()): w for w in wordlist[::-1]}
        print([words.get(w) or cap.get(w.lower()) or vowel.get(re.sub("[aeiou]", '#', w.lower()), "") for w in queries])


A=Solution()
#A.spellchecker(["v","t","k","g","n","k","u","h","m","p"], ["n","g","k","q","m","h","x","t","p","p"])
A.spellchecker(["KiTe","kite","hare","Hare"],["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])