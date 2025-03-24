from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
       
        meetings.sort()

        total_meeting_days = 0
        prev_start, prev_end = meetings[0]

        for start, end in meetings[1:]:
            if start <= prev_end + 1: 
                prev_end = max(prev_end, end)  
            else:
                total_meeting_days += (prev_end - prev_start + 1) 
                prev_start, prev_end = start, end 

      
        total_meeting_days += (prev_end - prev_start + 1)

       
        return days - total_meeting_days
