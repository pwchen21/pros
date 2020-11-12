def reverseWords(s):
	lists=s.split(" ")
	result=[]
	for word in lists:
		result.append(word[::-1])
	
	print ' '.join(result)


reverseWords("Let's take LeetCode contest")