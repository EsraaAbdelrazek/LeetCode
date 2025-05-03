
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the word to form the key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())
