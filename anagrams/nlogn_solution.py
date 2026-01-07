from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:        
    words = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        words[key].append(word)

    return list(words.values()) 
