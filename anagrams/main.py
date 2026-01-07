from anagrams.nlogn_solution import groupAnagrams

# Problem statement
###################
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.


if __name__ == '__main__':
    strs=["act","pots","tops","cat","stop","hat"]
    anagrams = groupAnagrams(strs)
    print(anagrams)
    strs=["",""]
    anagrams = groupAnagrams(strs)
    print(anagrams)