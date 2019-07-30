class Solution(object):
	def longestWord(self, words):
		ws=sorted(words)
		print ws
		'''
		words.sort(key=lambda x: (-len(x), x))
		d = set(words)
		print d
		for word in words:
			# break if word not in d
			if all(word[:i] in d for i in xrange(1, len(word))):
				# break if we have found the result
				print word
		return ''
		'''
A=Solution()
A.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])