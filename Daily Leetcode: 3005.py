''' For this solution: I made a dictionary to count the frequencies
Then I checked for the highest values and basically said if the value in the
dictionary was in the highest value, add the amount of times that key is there
'''
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        highest_value = 0
        for key,val in freq.items():
            if val > highest_value:
                highest_value = val
        total = 0
        for key,val in freq.items():
            if val == highest_value:
                total += val
        return total

        
