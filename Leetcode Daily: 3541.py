#3541. Find Most Frequent Vowel and Consonant

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = {'b': 0, 'c': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0, 
        'm': 0, 'n': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0
        }
        vowel = {'a': 0,'e': 0,'i': 0, 'o': 0, 'u': 0}
        best = 0
        vowel_sum = 0
        con_sum = 0
        for key in s:
            if ('a' in key or 'e' in key or 'i' in key or 'o' in key or 'u' in key):
                vowel[key] += 1
                continue
            alphabet[key] += 1

        for num in vowel.values():
            if num > vowel_sum:
                vowel_sum = num
        for num in alphabet.values():
            if num > con_sum:
                con_sum = num
                
        return(vowel_sum + con_sum)
        
        

