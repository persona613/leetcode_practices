"""
37 ms runtime beats 94.64%
16.5 MB memory beats 31.34%
"""
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        res = [0] * n
        i = 1
        # add: Aij = (i-1)*n + j
        # position: Pij = i*j + (n+(i-1)*n)*(i-1)/2
        Si = (i-1)*n*n + (1+n)*n//2 # row-sum
        while candies > Si:
            candies -= Si
            i += 1
            Si = (i-1)*n*n + (1+n)*n//2
        # print(i)
        for j in range(1, n+1):
            Aij = (i-1)*n + j
            # print(f"Aij: {Aij}, candies: {candies}")
            if candies > Aij:
                res[j-1] = i*j + (n+(i-1)*n)*(i-1)//2 # Pij
                candies -= Aij
            else:
                if candies != 0:
                    i -= 1 # change row to i-1
                    res[j-1] = i*j + (n+(i-1)*n)*(i-1)//2 + candies # P(i-1,j) + candies
                    candies = 0
                else:
                    res[j-1] = i*j + (n+(i-1)*n)*(i-1)//2
        return res

        # n = num_people
        # res = [0] * n
        # i = 1
        # while candies > i:
        #     res[(i-1) % n] += i
        #     candies -= i
        #     i += 1
        # res[(i-1) % n] += candies
        # return res