class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Character count of each string to the list of anagrams

        for s in strs:
            count = [0] * 26 #a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1 #Converts ascii value to a comprable index value for the count array

            result[tuple(count)].append(s)
            
        return result.values()

        # Runetime is O(m * n) where m is the length of the list and n is the average size of each word
