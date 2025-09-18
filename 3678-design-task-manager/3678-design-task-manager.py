import heapq

class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.h = []
        self.info = {}
        for u, t, p in tasks:
            self.info[t] = (u, p)
            heapq.heappush(self.h, (-p, -t, t))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.info[taskId] = (userId, priority)
        heapq.heappush(self.h, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        u, _ = self.info[taskId]
        self.info[taskId] = (u, newPriority)
        heapq.heappush(self.h, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.info:
            del self.info[taskId]

    def execTop(self) -> int:
        while self.h:
            np, nt, t = heapq.heappop(self.h)
            if t in self.info and self.info[t][1] == -np:
                u = self.info[t][0]
                del self.info[t]
                return u
        return -1