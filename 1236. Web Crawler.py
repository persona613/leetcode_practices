"""
177 ms runtime beats 73.36%
23.03 MB memory beats 72.30%
"""
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        seen = {startUrl}
        res = [startUrl]
        hostname = startUrl.split("/")[2]
        q = deque([startUrl])
        while q:
            curr = q.popleft()
            adjs = htmlParser.getUrls(curr)
            for adj in adjs:
                if adj not in seen:
                    seen.add(adj)
                    hname = adj.split("/")[2]
                    if hname == hostname:
                        res.append(adj)
                        q.append(adj)
        return res