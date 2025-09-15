1935. Maximum Number of Words You Can Type
"""This one for some reason I had a problem with instead of having a boolean that checks if each letter in the broken letter are in the each word of text
I added it to the check broken integer, which made it false because the check_broken will basically add 1 every single time the broken letter was in the world
which is bad because if two broken letters are in the same word, it will add two instead of 1, and basically I had to find out that using boolean was better.
"""

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        splits_words = text.split()
        split_letter = list(brokenLetters)
        good_word = 0
        for word in range(len(splits_words)):
            check_broken = False
            for letter in range(len(split_letter)):
                if split_letter[letter] in splits_words[word]:
                    check_broken = True
            if not check_broken:
                good_word += 1
        return good_word



        
