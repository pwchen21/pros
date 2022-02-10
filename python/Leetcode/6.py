class Solution:
    def convert(self, s, numRows):
        #gp=(len(s)-1)/2
        ans=''
        cur_id=[0, 0]
        mark='d' # down / up 
        AL=[[s[0]]]
        
        if numRows == 1:
            return s

        for x in range(1, numRows):
            AL.append([])
            

        print('AL now:', AL)

        for i in s[1:]:
            print('Now STR:', i)
            if mark == 'd':
                cur_id[1]=cur_id[1]+1
                print('  d, cur-id', cur_id)
                #AL[cur_id[0]][cur_id[1]]=i
                AL[cur_id[1]].append(i)
                print('     d, AL', AL)

                if cur_id[1] == numRows-1:
                    mark = 'u'
            elif mark == 'u':
                cur_id[0]=cur_id[0]+1
                cur_id[1]=cur_id[1]-1
                print('  u, cur-id', cur_id)
                #AL[cur_id[0]][cur_id[1]]=i
                AL[cur_id[1]].append(i)
                print('    u, AL', AL)
                if cur_id[1] == 0:
                    mark = 'd'
        print(AL)
        for x in range(len(AL)):
            ans=ans+''.join(AL[x])
        print(ans)

A=Solution()
A.convert('PAYPALISHIRING',4 )