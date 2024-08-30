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


# bottom up dynamic programing

#  we will start from the last step and work out way down
# say we start with 5 steps
# if we start at 5 then we only have one way gettig to 5 = 0 steps
# if we start at 4 we have only one way to get to 5 and thats one step
# if we start at 3 we take one step get to 4 and then we know 1 way to get to 5 from 4 
# or we can take 2 steps and get to 5
# from 2 we get 1 step to get to 3 and know that we have 2 ways to get to 5 from 3
# we can take 2 steps from 2 and get to 4 and then have one wya to get to 5
# this gives use 3 ways at 2
# at 1 we can get to 2 with 1 step and 3 with 3 2 steps and we know 2 has 3 ways and 3 has 2 ways so 1 has 5 ways
# and at 0 we have 1 step to 1 and two to 2 , 1 step has 5 ways to 5 and 2 has 3 ways that means step 0 is 8 ways and thats our answer 


class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the number of ways to reach the last step (step n) and the second to last step (step n-1)
        # Both initialized to 1 since there's only one way to stay on the last step or get to the last step from the second to last step
        current_step, prior_step = 1, 1
        #so current step = step 4 ad prior step = step 5
        # Loop through from step 4 down to step 1 (n - 1 iterations)
        # This loop builds the number of ways to reach the top from each step
        for i in range(n - 1):
            # Temporarily store the current number of ways to reach the last step from the current step
            temp = current_step
            print(current_step , prior_step)
            # Update current_step to be the sum of the ways from the current step and the prior step
            current_step = current_step + prior_step
            print(current_step , prior_step)
            # Iteration 1:step(5-1) new current = current_step = 1 , prior_step = 1 / start at step 3 have 2 options , 1 from 4 , 1 from 5
            # Iteration 2:step(4-1) new current = current_step = 2 , prior_step = 1 / start at step 2 have 3 options , 2 from 3 , 1 from 4
            # Iteration 3:step(3-1) new current = current_step = 3 , prior_step = 2 / start at step 1 have 5 options , 3 from 2 , 2 from 3    
            # Iteration 4:step(2-1) new current = current_step = 5 , prior_step = 3 / start at step 0 have 8 options , 5 from 1 , 3 from 2  
            # Total ways to climb 5 steps: 8

            # Update prior_step to the old value of current_step (before the update)
            prior_step = temp

        return current_step

# Example usage
sol = Solution()
print(f"Total ways to climb 5 steps: {sol.climbStairs(5)}")