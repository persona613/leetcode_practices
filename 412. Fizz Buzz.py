
'''
Runtime: 85 ms, faster than 15.03% of Python3 online submissions for Fizz Buzz.
Memory Usage: 14.9 MB, less than 85.02% of Python3 online submissions for Fizz Buzz.
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append('FizzBuzz')
            elif i % 5 == 0:
                answer.append('Buzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            else:
                answer.append(str(i))
        return answer