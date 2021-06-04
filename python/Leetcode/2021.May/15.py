class Solution:
    def isNumber(self, S: str) -> bool:    
        num, exp, sign, dec = False, False, False, False
        for c in S:
            print(c)
            if c >= '0' and c <= '9':
                num = True     
                print(num, exp,sign, dec)
            elif c == 'e' or c == 'E':
                if exp or not num: 
                    print(num, exp,sign, dec)
                    return False
                else:
                    num, exp, sign, dec = False, True, False, False
                    print(num, exp,sign, dec)
            elif c == '+' or c == '-':
                if sign or num or dec:
                    print(num, exp,sign, dec)
                    return False
                else: 
                    sign = True
                    print(num, exp,sign, dec)
            elif c == '.':
                if dec or exp:
                    print(num, exp,sign, dec)
                    return False
                else: 
                    dec = True
                    print(num, exp,sign, dec)
            else:
                print(num, exp,sign, dec)
                return False
        return num


A=Solution()
A.isNumber('99e2.5')