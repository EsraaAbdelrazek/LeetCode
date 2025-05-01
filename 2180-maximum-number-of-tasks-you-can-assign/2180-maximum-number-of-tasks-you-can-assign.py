from collections import deque
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
      
        # Define the 'check' function which tries to determine if 'x' tasks can be assigned to workers.
        def check(x: int) -> bool:
            task_index = 0
            workers_under_strength = deque()
            remaining_pills = pills
            for worker_index in range(num_workers - x, num_workers):
                # Assign as many tasks as possible to workers under their available strength plus pills boost
                while task_index < x and tasks[task_index] <= workers[worker_index] + strength:
                    workers_under_strength.append(tasks[task_index])
                    task_index += 1
                # If there are no more workers under strength to assign tasks, return False
                if not workers_under_strength:
                    return False
                # If the worker can do the task without a pill, pop it from the left
                if workers_under_strength[0] <= workers[worker_index]:
                    workers_under_strength.popleft()
                # If no pills are left, it's not possible to assign more tasks
                elif remaining_pills == 0:
                    return False
                # Otherwise, use a pill and give the worker the hardest task
                else:
                    remaining_pills -= 1
                    workers_under_strength.pop()
            return True

        # Get the number of tasks and workers
        num_tasks, num_workers = len(tasks), len(workers)
        # Sort tasks and workers in ascending order
        tasks.sort()
        workers.sort()

        # Set the initial binary search range
        left, right = 0, min(num_tasks, num_workers)
      
        # Perform a binary search to find the maximum number of tasks that can be assigned
        while left < right:
            mid = (left + right + 1) // 2  # Use integer division for Python 3
            if check(mid):
                left = mid  # If 'mid' tasks can be assigned, try a higher number
            else:
                right = mid - 1  # Otherwise, try a lower number

        # The 'left' variable now holds the maximum number of tasks that can be assigned
        return left