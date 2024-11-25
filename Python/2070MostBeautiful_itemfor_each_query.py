# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

# Example 1:

# Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
# Output: [2,4,5,5,6,6]
# Explanation:
# - For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
# - For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
#   The maximum beauty among them is 4.
# - For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
#   The maximum beauty among them is 5.
# - For queries[4]=5 and queries[5]=6, all items can be considered.
#   Hence, the answer for them is the maximum beauty of all items, i.e., 6.
# Example 2:

# Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
# Output: [4]
# Explanation: 
# The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
# Note that multiple items can have the same price and/or beauty.  

from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        output = []
        for num in queries:
            max_for_query = 0
            for item in items:
                if item[0] <= num:
                    max_for_query = max(item[1] , max_for_query)

            output.append(max_for_query)
        return output

        
sol = Solution
print(sol.maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]))


# more effecent solution


class Solution2:
    def maximumBeauty2(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price
        items.sort()
        
        # Sort queries along with their original indices
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        
        output = [0] * len(queries)  # To store results in the order of original queries
        max_for_query = 0
        start_index = 0

        for num, original_index in sorted_queries:
            # Find the maximum beauty for the current query
            while start_index < len(items) and items[start_index][0] <= num:
                max_for_query = max(max_for_query, items[start_index][1])
                start_index += 1
            output[original_index] = max_for_query  # Store result in original query order
        
        return output
sol = Solution2
print(sol.maximumBeauty2(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))