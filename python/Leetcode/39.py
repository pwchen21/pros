class Solution(object):
	def combinationSum(self, candidates, target):
		candidates.sort()			
		mtarget=target
		ans=[]
		count = 0
		def rec(count, ans, candidates, mtarget):
			print 'input(ans/candicates/mtarget): ' , ans, '/', candidates , '/', mtarget
			for x in candidates:
				print 'o-x:', x
				print 'o-mtarget', mtarget
				if x > mtarget:
					print "1-mtarget:", mtarget
					print '1-ans:', ans
					if ans:						
						mtarget=mtarget+ans.pop()
						print "if ans", mtarget
					break
				elif mtarget - x == 0:
					ans.append(x)
					print '2-mtarget',  mtarget
					print '2-ans:', ans
				else:
					print "3-mtarget", mtarget
					print "3-x", x
					ans.append(x)
					print '3-ans:' ,ans
					mtarget = mtarget - x 					
					count+=1
					print "==loop===" , count					
					rec(count, ans, candidates, mtarget)
					print "==loop end==", count
					
		rec(count, ans, candidates, mtarget)

A=Solution()
A.combinationSum([2,3,6,7], 7)