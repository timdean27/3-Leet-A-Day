# the students are provided with a string that consists of lowercase english letters. in one move they can shoose any index i and let the character at that index be c. then , the first occurance of c to the left of i and the first occurance of c to the right of i are deleted(note the operatiion can still be carried out evenn if either the left or tight occurance doesnt exist). for example , if word = "ababacaea" , and if index 4 is chosen (0-based), the first occuraence of 'a' to the left and right of index 4 are delted leaving word = "abdacea" 
# find the minium number of moves the students need to perform in order to get a word of minimal length

def getMinimumMoves(word):

    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    

    most_common_char = max(char_count, key=char_count.get)
    # find the letter that occurs the most
 
    middlemost_index = word.index(most_common_char)
    #find the middle occurance of the index

    # the minimum number of moves to create the shortes word(removing the most cahracter)
    # should be the maxium amount of occurances of the character 
    # on the left of the middle or the right of the middle 
    left_moves = right_moves = 0
    for i in range(middlemost_index):
        if word[i] != most_common_char:
            left_moves += 1
    for i in range(len(word) - 1, middlemost_index, -1):
        if word[i] != most_common_char:
            right_moves += 1
    
    return max(left_moves, right_moves)
# Example usage:
word = "ababacaea"
print(getMinimumMoves(word))  # Output: 1


