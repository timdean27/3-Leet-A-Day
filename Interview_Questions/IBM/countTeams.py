#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skills
#  2. INTEGER minPlayers
#  3. INTEGER minLevel
#  4. INTEGER maxLevel
#

def countTeams(skills, minPlayers, minLevel, maxLevel):
    # Filter the skills based on minLevel and maxLevel
    filtered_skills = [skill for skill in skills if minLevel <= skill <= maxLevel]
    n = len(filtered_skills)
    
    def count_combinations(n, k):
        print(k)
        # Count combinations without using binomial coefficients
        if k > n or k < 0:
            return 0
        if k == 0:
            return 1
        if k > n - k:  # Use the property C(n, k) = C(n, n-k)
            k = n - k
        count = 1
        for i in range(k):
            count = count * (n - i) // (i + 1)
        return count
    
    count = 0
    
    # Calculate number of ways to choose each possible team size from minPlayers to n
    for team_size in range(minPlayers, n + 1):
        count += count_combinations(n, team_size)
    
    return count

# Example usage
print(countTeams(skills = [6, 4, 8, 7, 5, 2], minPlayers = 2, minLevel = 3, maxLevel = 10))
