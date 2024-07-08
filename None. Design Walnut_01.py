"""
41 / 42 test cases passed.
Status: Wrong Answer
Submitted: 0 minutes ago
Input:
["Walnut","parseText","parseText","getTotalUserEarnings","getTotalUserExpenses","getAverageUserEarnings","getAverageUserExpenses"]
[[],[1,"credit .01"],[2," debit1."],[1],[2],[],[]]
Output:
[null,null,null,0.00000,1.00000,0.00000,1.00000]
Expected:
[null,null,null,0.01000,1.00000,0.00500,0.50000]
"""
class Walnut:

    def __init__(self):
        self.users = dict()
        self.total_user_earning = 0
        self.total_user_expense = 0
        self.valid_earn_words = {"credit", "credited", "deposit", "deposited"}
        self.valid_expense_words = {"debit", "debited", "withdraw", "withdrawal", "withdrawn"}
        self.valid_amount = {"USD x", "x USD", "USDx", "$ x", "x $", "$x"}

    def parseText(self, userID: int, text: str) -> None:
        ret = self.validtext(text)
        if not ret:
            return
        
        user = self.users.setdefault(userID, User(userID))
        kind = ret[0]
        money = float(ret[1])
        if kind == 0:
            user.earning.append(money)
            user.total_earning += money
            self.total_user_earning += money
        else:
            user.expense.append(money)
            user.total_expense += money
            self.total_user_expense += money

    def getTotalUserEarnings(self, userID: int) -> float:
        if userID not in self.users:
            return 0
        return self.users[userID].total_earning        

    def getTotalUserExpenses(self, userID: int) -> float:
        if userID not in self.users:
            return 0
        return self.users[userID].total_expense

    def getAverageUserEarnings(self) -> float:
        if not self.users:
            return 0
        return self.total_user_earning / len(self.users)        

    def getAverageUserExpenses(self) -> float:
        if not self.users:
            return 0
        return self.total_user_expense / len(self.users)
        
    def validtext(self, text) -> list: # [earn/expense, number string]
        
        # check earning or expense        
        # (?:pattern)=匹配但不捕獲文本, \b=字的邊界, ?=匹配前面字元零次或一次
        ret1 = re.findall(r"\bcredit(?:ed)?\b|\bdeposit(?:ed)?\b", text, re.I)
        # print(f"{ret1 = }")
        
        ret2 = re.findall(r"\bdebit(?:ed)?\b|\bwithdraw(?:al|n)?\b", text, re.I)
        # print(f"{ret2 = }")
        if (ret1 and ret2) or (not ret1 and not ret2):
            return []
        
        # valid amount
        # check prefix
        ret3 = re.findall(r"(?:\bUSD|\$) ?[0-9]+\.?[0-9]*\b", text, re.I)
        # check surfix
        ret4 = re.findall(r"\b[0-9]+\.?[0-9]* (?:USD|\$)\b", text, re.I)
        if (not ret3 and not ret4) or len(ret3) + len(ret4) > 1:
            return []
        
        amount_list = ret3 if ret3 else ret4
        # print(f"{amount_list = }")
        amount_list = re.findall(r"[0-9]+(?:\.[0-9]*)?", amount_list[0])
        # print(f"{amount_list = }")
        
        # valid amount
        numstr = self.validamo(amount_list[0])
        if numstr == "":
            return []
        
        if ret1:
            return [0, numstr]
        else:
            return [1, numstr]

    def validamo(self, numstr) -> str:
        arr = numstr.split(".")
        bigpart = arr[0]
        if len(bigpart) == 10:
            if bigpart != "1000000000":
                return ""
            if len(arr) > 1:
                secpart = arr[1]
                if secpart and int(secpart):
                    return ""
        if len(arr) > 1:
            secpart = arr[1]
            if len(secpart) > 2:
                return ""
        return numstr
        
              
class User:
    
    def __init__(self, uid):
        self.id = uid
        self.earning = []
        self.expense = []
        self.total_earning = 0
        self.total_expense = 0

# Your Walnut object will be instantiated and called as such:
# obj = Walnut()
# obj.parseText(userID,text)
# param_2 = obj.getTotalUserEarnings(userID)
# param_3 = obj.getTotalUserExpenses(userID)
# param_4 = obj.getAverageUserEarnings()
# param_5 = obj.getAverageUserExpenses()