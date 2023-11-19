from collections import Counter

def most_frequent_char(string):
    if not string:
        return None, 0  # Return None if the string is empty

    # Use Counter to count the occurrences of each character
    char_counts = Counter(string)

    # Find the most common character and its frequency
    most_common_chars = char_counts.most_common(1)

    if not most_common_chars:
        return None, 0  # Return None if there are no characters in the string

    most_common_char, frequency = most_common_chars[0]

    return most_common_char, frequency

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == k:
            return k

        if len(s) == 1:
            return 1
        i = 0
        j = k-1
        max_length = 0
        while j < len(s):
            print(i,j)
            most_common_char, frequency = most_frequent_char(s[i:j+1])
            

            num_open_spaces = j-i+1 - frequency
            print(num_open_spaces,frequency)
            if num_open_spaces <= k:
                max_length = max(max_length,j-i+1)

            elif num_open_spaces > k:
                i = i+1
                

            j = j+ 1
        return max_length
