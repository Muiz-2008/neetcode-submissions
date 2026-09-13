class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary_words = defaultdict(list) 

        for each_word in strs:
            map_letters = [0] * 26

            for each_letter in each_word:
                map_letters[ord(each_letter) - ord("a")] += 1
            dictionary_words[tuple(map_letters)].append(each_word)

        return list(dictionary_words.values())

