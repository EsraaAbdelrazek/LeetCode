class Solution:
    def convertDateToBinary(self, date: str) -> str:
        res = ''
        datels = date.split ('-')
        print (datels)
        for i in range(len(datels)):
            
            res += str(bin(int(datels[i])))[2:]
         
            res += '-'

        return res [:-1]

        