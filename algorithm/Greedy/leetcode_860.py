#https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand = {"5":0, "10":0, "20":0}
        moneys = [10, 5]
        for bill in bills:
            hand[str(bill)] += 1
            correct = bill-5
            for money in moneys:
                while True:
                    if correct - money >= 0 and hand[str(money)] != 0:
                        correct -= money
                        hand[str(money)] -= 1
                    else:
                        break
            if correct != 0:
                return False
        return True
