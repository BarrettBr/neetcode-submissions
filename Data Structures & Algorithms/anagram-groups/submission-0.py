class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        mini = []
        for index in range(len(strs)):
            word = str()
            uniqueLetters = sorted(set(strs[index]))
            for letter in uniqueLetters:
                word += str(letter + str(strs[index].count(letter)))
            if word in mini:
                anagram[mini.index(word)].append(strs[index])
            else:
                mini.append(word)
                anagram.append([strs[index]])
        return anagram