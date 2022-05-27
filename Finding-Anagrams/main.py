# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    lword = list(word.lower().replace(' ',  ''))
    lanagram = list(anagram.lower().replace(' ', ''))
    if len(lword) != len(lanagram):
            return False
    for i in range(0, len(lanagram)):
        if lanagram[i] in lword:
            lword.remove(lanagram[i])
    if len(lword) == 0:
        return True    
    return False
