def num_divisors(n):
    return sum(n % i == 0 for i in range(1, n+1))

def solution(n):
    return sum(num_divisors(i) >= 3 for i in range(1, n+1))