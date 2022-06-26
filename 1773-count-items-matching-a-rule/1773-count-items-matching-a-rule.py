class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        itemMatched = 0
        ruleDict = {"type": 0, "color":1, "name":2}
        ruleIndex = ruleDict[ruleKey]
        for i in items:
            if i[ruleIndex] == ruleValue:
                itemMatched += 1
        
        return itemMatched