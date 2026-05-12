class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # sort by (minimum - actual) in descending order
        tasks.sort(
            key=lambda x: x[1] - x[0],
            reverse=True
        )

        ans = 0
        energy = 0

        for i in range(len(tasks)):

            actual = tasks[i][0]
            minimum = tasks[i][1]

            # increase initial energy if needed
            if energy < minimum:
                ans += (minimum - energy)
                energy = minimum

            # perform task
            energy -= actual

        return ans