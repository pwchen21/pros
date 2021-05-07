class Solution:
	def findLongestWord(self, s,d):
		T=sorted([len(x), x] for x in d)
		print(T)

		max_len=0
		ans_temp=[]
		flag=0
		for z in T[-1::-1]: #monkey
			t=-1
			print('1. words:', z[1])
			cp=0
			if not ans_temp:
				max_len=len(z[1])
			elif len(z[1]) == max_len:
				print('here')
				pass;
			else:
				break;

			for x in z[1]: #m.o.n.k.e.y
				print('  2.x:', x )
				cp=0
				#for y in range(t+1, len(s)): #abpcplea
				while t < len(s)-1:
					t=t+1
					#print('	3.t+1:', t)
					#print('      3.y, s[t]', t, '/', s[t])
					if x == s[t]:
						cp = 1
						print('       4.t/count:', t)
						print('       4.s[t]:', s[t])
						break
					else:
						cp = 0
				if cp == 0:
					break
			if cp == 1:
				ans_temp.append(z[1])
				print('      5.ans_temp', ans_temp)

		if ans_temp:
			print(sorted(ans_temp))
			print (sorted(ans_temp)[0])
			return (sorted(ans_temp)[0])
		else:
			print('ans is empty string')
			return ""
A=Solution()
A.findLongestWord("abpcplea", ["ale","apple","pcple","plea", "dddd"])
print("=========")
A.findLongestWord("bab", ["ba","ab","a","b"])
print("=========")
A.findLongestWord("aewfafwafjlwajflwajflwafj", ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"])
print("=========")
A.findLongestWord("okbmfyugqqongobwofraotanviqjraaktmmwyxzdnnwwaqsnvfxwngglybtiqwblprgvbgmolotnppzbovnstxmcmocixresdpojmntcdkyjzgbhhigkiyatrgzayivjyqiopvvdftkbsgwgnidsecvydvltaxxywydawrsseyolixznuyhjolngdsmjhepregixtklanjjggzssrbtmhhpamcfeghgssmrjrpelabojfhkdfvscjwhqxubwrhryqmtkiksljezeembngdjyhgmdzahxvvpkqwvhkqlensuxbrcdctqojqnlogjbpovdsbvurwcoehtmtkwxswrwhszuyesdqspnwqxlmjxrbdqbnbbyxhhlabxrdjxtjgpugojsexmrhrfzryapdzglalqzuzfpxeaemjkyfhpbnmdxjtxnxyjecfsapcjyglmtivnsfalpxzdkylgcixjljaqjwminyaodeekpzzpchhceguzayeul", ["xcjigjydkponyjablqgulfhcyzbtbdocvsxzwzdabvbnzxzxcawydbbsuexdxpvmtjcxdgdcdxgccjfciphjmubucghqfqoqqugnvbblziedkifhyrkzugorbalkggrhingdsnfnvbofjunyuzjfmnpqloxtshyxyaavbskikosutlqeljnycostvxqviixgspazzitxhiujcqnatfwechwzuoxxwibszywniscleusciwjvcfcocneuaizzgluudughrvgozsgvrpcwsjzivzpbzfjqshrdckfcxjsgwcrhcmntpkezibuegxduskenhrhuayysefshuwokduoaibwpcrssypqflhqeipzsyiycrbtblfnwozngtcddepfxyhvfjcoxytxqkfgzduzzjjqdauxxgjhxqaewlihotqibnskdluickwaakwvopgatumfndzcjieoncdwmhfgpvtegeawueivtnyumvwxuzfcaxeuremvv"])
print("=========")
A.findLongestWord("okbmfyugqqongobwofraotanviqjraaktmmwyxzdnnwwaqsnvfxwngglybtiqwblprgvbgmolotnppzbovnstxmcmocixresdpojmntcdkyjzgbhhigkiyatrgzayivjyqiopvvdftkbsgwgnidsecvydvltaxxywydawrsseyolixznuyhjolngdsmjhepregixtklanjjggzssrbtmhhpamcfeghgssmrjrpelabojfhkdfvscjwhqxubwrhryqmtkiksljezeembngdjyhgmdzahxvvpkqwvhkqlensuxbrcdctqojqnlogjbpovdsbvurwcoehtmtkwxswrwhszuyesdqspnwqxlmjxrbdqbnbbyxhhlabxrdjxtjgpugojsexmrhrfzryapdzglalqzuzfpxeaemjkyfhpbnmdxjtxnxyjecfsapcjyglmtivnsfalpxzdkylgcixjljaqjwminyaodeekpzzpchhceguzayeul", ["xcjigjydkponyjablqgulfhcyzbtbdocvsxzwzdabvbnzxzxcawydbbsuexdxpvmtjcxdgdcdxgccjfciphjmubucghqfqoqqugnvbblziedkifhyrkzugorbalkggrhingdsnfnvbofjunyuzjfmnpqloxtshyxyaavbskikosutlqeljnycostvxqviixgspazzitxhiujcqnatfwechwzuoxxwibszywniscleusciwjvcfcocneuaizzgluudughrvgozsgvrpcwsjzivzpbzfjqshrdckfcxjsgwcrhcmntpkezibuegxduskenhrhuayysefshuwokduoaibwpcrssypqflhqeipzsyiycrbtblfnwozngtcddepfxyhvfjcoxytxqkfgzduzzjjqdauxxgjhxqaewlihotqibnskdluickwaakwvopgatumfndzcjieoncdwmhfgpvtegeawueivtnyumvwxuzfcaxeuremvv", "mfuraildmrjhdjtctdxejgdurr"])
print("=========")
A.findLongestWord("abc", ["bcftftghghgh"])