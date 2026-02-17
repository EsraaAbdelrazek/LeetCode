class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = [] 

        for h in range (12) : 
            for m in range (60) : 
                h_ones = bin(h).count ('1')
                m_ones = bin(m).count ('1')

                if (h_ones + m_ones) == turnedOn  : 
                    times.append(f"{h}:{m:02d}")
        return times

        