class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        broken = list(brokenLetters)
        
        for l in broken:
            words = [x for x in words if l not in x]
        
        return len(words)
        