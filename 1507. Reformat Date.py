"""
30 ms runtime beats 83.93%
16.72 MB memory beats 26.85%
"""
class Solution:
    def reformatDate(self, date: str) -> str:
        ms1 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        ms2 = [f"{x:02n}" for x in range(1, 13)]
        dic = {k: v for k, v in zip(ms1, ms2)}
        date = date.split()
        date[0] = f"{int(date[0][-3::-1][::-1]):02n}"
        date[1] = dic[date[1]]
        return "-".join(date[::-1])