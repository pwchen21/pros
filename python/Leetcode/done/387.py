import itertools
def firstUniqChar(s):
	news=[]
	for x in s:
		if x not in news:
			news.append(x)
	print news
	for w in news:
		if s.count(w) == 1:
			print s.index(w)
	print -1
			
print("==")
firstUniqChar('leetcode')
print("==")
firstUniqChar('loveleetcode')
print("==")
firstUniqChar('llee')