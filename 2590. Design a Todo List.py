"""
161 ms runtime beats 95.08%
18.64 MB memory beats 62.30%
"""
class TodoList:

    def __init__(self):
        self.taskid = 1
        # heapq lazy delete
        # {user id: [[dueDate, task id]]}
        self.users_queue = defaultdict(list)
        # {task id: task class}
        self.taskfinder = dict()

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        taskid = self.taskid
        self.taskid += 1
        heapq.heappush(self.users_queue[userId], [dueDate, taskid])

        newtask = Task(userId, taskid, taskDescription, dueDate, tags)
        self.taskfinder[taskid] = newtask
        return taskid

    def getAllTasks(self, userId: int) -> List[str]:
        res = []
        temp = []
        q = self.users_queue[userId]
        while q:
            duedate, taskid = heapq.heappop(q)
            curr_task = self.taskfinder[taskid]
            if curr_task.complete is False:
                temp.append([duedate, taskid])
                res.append(curr_task.descri)
        self.users_queue[userId] = temp
        return res

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        res = []
        temp = []
        q = self.users_queue[userId]
        while q:
            duedate, taskid = heapq.heappop(q)
            curr_task = self.taskfinder[taskid]
            if curr_task.complete is False:
                temp.append([duedate, taskid])
                if tag in curr_task.tags:
                    res.append(curr_task.descri)
        self.users_queue[userId] = temp
        return res

    def completeTask(self, userId: int, taskId: int) -> None:
        if taskId not in self.taskfinder:
            return
        task = self.taskfinder[taskId]
        if task.user != userId:
            return
        task.complete = True

class Task:

    def __init__(self, userid, taskid, descri, duedate, tags):
        self.user = userid
        self.id = taskid
        self.descri = descri
        self.duedate = duedate
        self.tags = set(tags)
        self.complete = False


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)