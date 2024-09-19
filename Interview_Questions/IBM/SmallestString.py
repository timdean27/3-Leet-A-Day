def getSmallestString(word, substr):
    lengthW = len(word)
    lengthS = len(substr)
    
    # If substring cannot fit in the word
    if lengthS > lengthW:
        return -1
    
    smallest_string = None
    
    # Iterate through all possible positions for substr in word
    for i in range(lengthW - lengthS + 1):
        # Create a list to modify the word
        temp_word = list(word)
        
        valid = True
        for j in range(lengthS):
            if temp_word[i + j] != '?' and temp_word[i + j] != substr[j]:
                valid = False
                break
            temp_word[i + j] = substr[j]
        
        if not valid:
            continue
        
        # Replace remaining '?' with 'a'
        temp_word = [char if char != '?' else 'a' for char in temp_word]
        candidate_string = ''.join(temp_word)
        
        # Update smallest_string if this candidate is smaller
        if smallest_string is None or candidate_string < smallest_string:
            smallest_string = candidate_string
    
    return smallest_string if smallest_string is not None else -1

# Example usage
print(getSmallestString(word="as?b?e?gf", substr="dbk"))
