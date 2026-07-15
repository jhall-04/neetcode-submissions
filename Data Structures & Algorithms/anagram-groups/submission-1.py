class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for w in strs:
            counts = [0] * 26
            for c in w:
                counts[ord(c) - 97] = counts[ord(c) - 97] + 1
            key = tuple(counts)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(w)
        return list(anagrams.values())
