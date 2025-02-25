class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)  # Move one step
            fast = get_next(get_next(fast))  # Move two steps

        return fast == 1
