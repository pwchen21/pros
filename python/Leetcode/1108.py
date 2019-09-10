class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        IP=address.split('.')
        print('[.]'.join(IP))

A=Solution()
A.defangIPaddr("10.1.1.23")