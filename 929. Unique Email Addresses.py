"""
55 ms runtime beats 98.54%
16.5 MB memory beats 18.36%
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = defaultdict(set)
        cnt = len(emails)
        for mail in emails:
            loc, dom = mail.split("@")
            loc = loc.split("+")[0].replace(".", "")
            if loc in dic and dom in dic[loc]:
                cnt -= 1
            else:
                dic[loc].add(dom)
        return cnt
