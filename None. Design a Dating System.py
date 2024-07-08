"""
893 ms runtime beats None %
20.6 MB memory beats None %
"""
class Tinder:

    def __init__(self):
        self.users = dict()

    def signup(self, userId: int, gender: int, preferredGender: int, age: int, minPreferredAge: int, maxPreferredAge: int, interests: List[str]) -> None:
        new_user = User(userId, gender, preferredGender, age, minPreferredAge, maxPreferredAge, interests)
        self.users[userId] = new_user

    def getMatches(self, userId: int) -> List[int]:
        if userId not in self.users:
            return
        
        q = []
        curr_user = self.users[userId]
        preferGender = curr_user.preferredGender
        minpreAge = curr_user.minPreferredAge
        maxpreAge = curr_user.maxPreferredAge
        curr_interests = curr_user.interests
        
        for uid in self.users:
            if uid == userId:
                continue
            candidate = self.users[uid]
            if candidate.gender == preferGender and minpreAge <= candidate.age <= maxpreAge:
                common_interests = curr_interests.intersection(candidate.interests)
                if common_interests:
                    heapq.heappush(q, (-len(common_interests), candidate.uid))
                    
        res = []
        while q and len(res) < 5:
            t, uid = heapq.heappop(q)
            res.append(uid)
        return res
                
        
        
class User:
    
    def __init__(self, userId, gender, preferredGender, age, minPreferredAge, maxPreferredAge, interests):
        self.uid = userId
        self.gender = gender
        self.preferredGender = preferredGender
        self.age = age
        self.minPreferredAge = minPreferredAge
        self.maxPreferredAge = maxPreferredAge
        self.interests = set(interests)

# Your Tinder object will be instantiated and called as such:
# obj = Tinder()
# obj.signup(userId,gender,preferredGender,age,minPreferredAge,maxPreferredAge,interests)
# param_2 = obj.getMatches(userId)