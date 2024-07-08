"""
514 ms runtime beats None %
32 MB memory beats None %
"""
class WhatsApp:

    def __init__(self):
        self.group_id = 1
        # {id: set{users}}
        self.group = dict()
        # {user id: [received message]}
        self.messages = defaultdict(list)

    def sendMessage(self, toUser: int, message: str) -> None:
        self.messages[toUser].append(message)

    def createGroup(self, initialUsers: List[int]) -> int:
        self.group[self.group_id] = set(initialUsers)
        self.group_id += 1
        return len(self.group)

    def addUserToGroup(self, groupId: int, userId: int) -> None:
        if groupId in self.group:
            self.group[groupId].add(userId)

    def sendGroupMessage(self, fromUser: int, groupId: int, message: str) -> None:
        if groupId not in self.group or fromUser not in self.group[groupId]:
            return
        for user in self.group[groupId]:
            if user != fromUser:
                self.messages[user].append(message)

    def getMessagesForUser(self, userId: int) -> List[str]:
        return self.messages[userId][::-1]


# Your WhatsApp object will be instantiated and called as such:
# obj = WhatsApp()
# obj.sendMessage(toUser,message)
# param_2 = obj.createGroup(initialUsers)
# obj.addUserToGroup(groupId,userId)
# obj.sendGroupMessage(fromUser,groupId,message)
# param_5 = obj.getMessagesForUser(userId)