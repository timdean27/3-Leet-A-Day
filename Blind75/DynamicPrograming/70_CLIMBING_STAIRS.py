# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step



class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        options_to_get_to_current_step = [0] *(n+1)
        # fill with zeros 
        options_to_get_to_current_step[1] = 1
        # one option to get to step 1 
        options_to_get_to_current_step[2] = 2
        # two options to get to step 2

        for i in range(3,n+1):
            # the options to get to currnet step starting at 3 are the some of the options to get to one step under or 2 steps under
            # so we are taking 1 or 2 steps to get to current and we know have stored the number of ways to get to those prior steps already
            options_to_get_to_current_step[i] = options_to_get_to_current_step[i - 1] + options_to_get_to_current_step[i - 2]


            # example with 5 steps
            # we have one option to get to 1 and 2 options to get to 2
            # to get to 3 we get there from steps 1 or 2 and we know 1 = 1 option 2 = 2 options so we now have 3 options to get to 3
            # to get to 4 we can get there from step 2 or 3 and we have 2 options to 2 and 3 optiosn to 3 this make 5 options to 4
            # to get to 5 we can go from 3 or 4 and we have 3 options to 3 adn 5 options to 4 so we have 8 options to 5

sol = Solution()
print(f"Total ways to climb 5 steps: {sol.climbStairs(5)}")