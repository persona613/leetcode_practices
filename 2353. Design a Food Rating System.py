"""
786 ms runtime beats 45.24%
47.17 MB memory beats 68.45%
"""
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.entry_find = {}
        self.d = defaultdict(list)
        self.remove = "remove"
        for i in range(len(foods)):
            food = foods[i]
            self.entry_find[food] = [-ratings[i], cuisines[i], food]
        for k in sorted(self.entry_find.keys()):
            entry = self.entry_find[k]
            heapq.heappush(self.d[entry[1]], entry)

    def changeRating(self, food: str, newRating: int) -> None:
        entry = self.entry_find[food]
        cuisine = entry[1]
        entry[-1] = self.remove
        # create new entry
        entry = [-newRating, cuisine, food]
        self.entry_find[food] = entry
        heapq.heappush(self.d[cuisine], entry)        

    def highestRated(self, cuisine: str) -> str:
        curr = self.d[cuisine][0][-1]
        while curr == self.remove:
            heapq.heappop(self.d[cuisine])
            curr = self.d[cuisine][0][-1]
        return curr
        

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)