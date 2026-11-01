# Count Primes (Medium)
# https://leetcode.com/problems/count-primes/
# Accepted 2026-11-01 — Python3, runtime 2164 ms, memory 65.9 MB
class Solution:
    def countPrimes(self, n: int) -> int:
        
        '''
        a number is prime if it can only be divided by 1 and itself 
        0-9
        '''
        if n<3:
            return 0
        is_prime=[True]*n
        is_prime[0]=is_prime[1]=False

        for i in range(2, math.isqrt(n-1)+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j]=False
        return sum(1 for i in range(len(is_prime)) if is_prime[i])
